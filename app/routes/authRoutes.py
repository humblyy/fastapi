
from fastapi import HTTPException,status,APIRouter,Depends

router=APIRouter(tags=["authentication"])

from app.database import get_db


from sqlalchemy.orm import Session
from app import models
from app.utils import verify_password
from app.oauth2 import create_jwt_token

# from ..database import get_db
# from sqlalchemy.orm import Session
# from .. import models
# from ..utils import verify_password
# from ..oauth2 import create_jwt_token
from fastapi.security import OAuth2PasswordRequestForm
# login

@router.post("/login")
# user:schemas.CreateUser,db:Session=Depends(get_db)
def user_login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    fetch_user=db.query(models.User).filter(models.User.email==user.username).first()
    if not fetch_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentails")
    checkUser=verify_password(user.password,fetch_user.password)

    if not checkUser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentails")
    
    payload={"user_id":fetch_user.id}
    jwt_token=create_jwt_token(payload)
 
    return {"token":jwt_token,"token_type":'bearer'}
