from fastapi.testclient import TestClient

from app import schemas


from jose import jwt
from app.envConfig import settings

import pytest





# def test_root(client):
#     res=client.get("/")
#     assert res.json().get("msg")=="welcome to the home page"
#     assert res.status_code==200
   
    
#     print(res.json().get("msg"))

def test_create_user(client):
    res=client.post("/users/",json={"email":"mrlu@gmail.com","password":"0000"})
    new_user=schemas.UserResponse(**res.json())
    # print(res.json().get("email"))
    assert new_user.email=="mrlu@gmail.com"
    # assert res.json().get("email")=="jaja@gmail.com"


JWT_SECRET_KEY=settings.jwt_secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRES=settings.access_token_expires
# test login
def test_login(test_user,client):
    res=client.post("/login",data={"username":test_user["email"],"password":test_user["password"]})
    login_res=schemas.Token(**res.json())
    payload=jwt.decode(login_res.token,JWT_SECRET_KEY,algorithms=ALGORITHM)
    user_id=payload.get("user_id")
    assert user_id==test_user["id"]
    assert login_res.token_type== "bearer"
    assert res.status_code==200

# check both for password and email
@pytest.mark.parametrize("email,password ,status_code",[("wrongemail",0000,403)])
def test_login_failed(test_user,client,email,password,status_code):

    res=client.post("/login",data={"username":test_user["email"],"password":"wrong password"})
    assert res.status_code==status_code
    assert res.json().get("detail")=="invalid credentails"