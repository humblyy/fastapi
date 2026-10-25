

from jose import JWTError,jwt
from datetime import timedelta,datetime

from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app import schemas
from app.envConfig import settings

# from .database import get_db
# from . import models
# from . import schemas
# from .envConfig import settings

JWT_SECRET_KEY=settings.jwt_secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRES=settings.access_token_expires

# create jwt token
def create_jwt_token(payload:dict):
    payload_to_encode=payload.copy()
    expire_date=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    payload_to_encode.update({"exp":expire_date})
    token=jwt.encode(payload_to_encode,JWT_SECRET_KEY,algorithm=ALGORITHM)

    return token


# verify user token

def verify_token(token:str,credentials_exceptions):
    try:
        payload=jwt.decode(token,JWT_SECRET_KEY,algorithms=ALGORITHM)
        user_id=payload.get("user_id")
        if user_id ==None:
            raise credentials_exceptions
        user_info=schemas.token_data(id=user_id)
        return user_info
    except JWTError:
        raise credentials_exceptions
    

# route protector function

oauth2_schema=OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):

    credentials_exceptions=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="couldn't validate credentials",headers={"WWW-Authenticate":"Bearer"})

    token_data=verify_token(token,credentials_exceptions)
    user=db.query(models.User).filter(models.User.id==token_data.id).first()


    return user
       
   