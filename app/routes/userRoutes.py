

from fastapi import Depends,HTTPException,status,APIRouter



# db connection for alchemy
from app import schemas
from app import models  
from app.database import engine,get_db
from sqlalchemy.orm import Session

# from .. import schemas
# from .. import models  
# from ..database import engine,get_db
# from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/users",
    tags=["users"]
    )
# hash
from app.utils import hash_fun
# from ..utils import hash_fun
models.Base.metadata.create_all(bind=engine)



# create user
@router.post("/",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.CreateUser,db:Session=Depends(get_db)):

#    salt = bcrypt.gensalt(rounds=12)
#    password_bytes = user.password.encode('utf-8')
#    hashed_bytes=bcrypt.hashpw(password_bytes,salt)
#    hashed_password_str = hashed_bytes.decode('utf-8')
#   email=user.email,password=hashed_password_str
    hashed_password=hash_fun(user.password)
    # dict() same as model_dump
    user.password=hashed_password
    new_user= models.User(**user.model_dump()) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



# retrive user

@router.get("/{user_id}",response_model=schemas.UserResponse)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user
    
