



from fastapi import Depends,HTTPException,status,Response,APIRouter

from typing import List, Optional


from .. import schemas
from .. import models  
from database import get_db
from sqlalchemy.orm import Session
import oauth2
from sqlalchemy import func

router=APIRouter(
    prefix="/posts",
    tags=["posts"]
)



# get posts using sqlalchemy
@router.get('/',response_model=List[schemas.postOut])
def get_post(db:Session =Depends(get_db),current_user:int=Depends(oauth2.get_current_user),limit:int=5,skip:int=0,search:Optional[str]=""):
    
    # # add query parameter limit ,search,skip
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit=query).offset(skip).all()

    # add likes
    result=db.query(models.Post,func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Post.id==models.Votes.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
 

    return result

# get own list of posts using sqlalchemy
@router.get('/somer-person',response_model=List[schemas.postOut])
def single_person_posts(db:Session =Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    posts=db.query(models.Post).filter(models.Post.user_id==current_user.id).all()
   
    return posts


# get one item
# @router.get("/{post_id}",response_model=schemas.ResponseSchema)
@router.get("/{post_id}",response_model=schemas.postOut)
def single_post(post_id:int,db:Session =Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):

    # post=db.query(models.Post).filter(models.Post.id==post_id).first()
    
    post=db.query(models.Post,func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Post.id==models.Votes.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.id==post_id).first()
    if post==None:
        raise HTTPException(status_code=404,detail="not post found with this id")
    
    ##add this if the owner only can see his post
    # if post.user_id!=current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not authorized to perform this action")
    return post



# create post using alchemy

@router.post('/',response_model=schemas.ResponseSchema,status_code=status.HTTP_201_CREATED)
def create_post(post:schemas.CreateSchema,db:Session =Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
   print(current_user)
#    ** for un packing the dictionary
##use this if the ownner can only see all the posts
#    new_post= models.Post(user_id=current_user.id,**post.dict())

   new_post= models.Post(user_id=current_user.id,**post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post



    



# delete item
@router.delete("/{post_id}")
def delete_post(post_id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    deleted_post=db.query(models.Post).filter(models.Post.id==post_id)
    if deleted_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="this post is not found")
    # only the owner can delete his post
    if deleted_post.first().user_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not authorized to perform this action")

    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_200_OK)




# using update
@router.put("/{post_id}",response_model=schemas.ResponseSchema)
def update_post(post_id:int,post:schemas.CreateSchema,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    query=db.query(models.Post).filter(models.Post.id==post_id)
    check_post=query.first()
    if check_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="the post with this id is not found")
    # #add this for if the only the person who posts can only update his posts
    if query.first().user_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not authorized to perform this action")

    query.update(post.dict(),synchronize_session=False)
    db.commit()
    return check_post



