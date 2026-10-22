

# hash using bcrypt algorithm

from passlib.context import CryptContext
password_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

# hash password
def hash_fun(password:str):
    return password_context.hash(password)

# compare input and hashed password
def verify_password(plain_password,hashed_password):
    return password_context.verify(plain_password,hashed_password)