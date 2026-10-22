

from fastapi import HTTPException,Depends,APIRouter,status
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
import oauth2
router=APIRouter(
    prefix="/votes",
    tags=["votes"]
)


@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # check if the post is found
    post=db.query(models.Post).filter(models.Post.id==vote.post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="this post does not exist")
    # check if the post have a vote and the login user has already voted
    query=db.query(models.Votes).filter(models.Votes.post_id==vote.post_id,models.Votes.user_id==current_user.id)
    userVoted=query.first()
    
    if vote.dir==1:
        if userVoted:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="user already voted this post")
        new_vote=models.Votes(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"msg":"you liked the post"}
    else:
        if not userVoted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="vote not found")

        query.delete(synchronize_session=False)
        db.commit()
        return {"msg":"you removed the like from the post"}
 
