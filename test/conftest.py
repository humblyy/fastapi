




from fastapi.testclient import TestClient
from app.orm import app

from app.database import get_db

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from app import models
import pytest
from app.oauth2 import create_jwt_token,verify_token

# establish connection between database and sqlalchemy
SQLALCHEMY_DATABASE_URL=f'postgresql://postgres:0000@localhost/test_social'
engine=create_engine(SQLALCHEMY_DATABASE_URL)

TestingsessionLocal=sessionmaker(autoflush=False,bind=engine,expire_on_commit=False)





@pytest.fixture
def session():
   
    models.Base.metadata.drop_all(bind=engine)
    # create the tables
    models.Base.metadata.create_all(bind=engine)
    db=TestingsessionLocal()
    try:
        yield db
    finally:
        db.close()




# create fixture to pass duplicate constriant
@pytest.fixture
def client(session):
    def override_get_db():
        
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    
    
    yield TestClient(app)




@pytest.fixture
def test_user(client):
    user_data={
        "email":"yimermoke@gmail.com",
        "password":"0000"
    }
    res=client.post("/users/",json=user_data)
    assert res.status_code==201
    new_user=res.json()
    new_user["password"]=user_data["password"]
    return new_user




# # posts test
# @pytest.fixture
# def token(test_user):
#     return create_jwt_token({"user_id":test_user["id"]})


# @pytest.fixture
# def authorized_client(client,token):
#     client.headers={
#         **client.headers,
#         "Authorization":f"Bearer {token}"
#     }
#     return client

# @pytest.fixture
# def test_post(test_user,session):
#     test_data=[
#         {"title":"here is the first title",
#          "content":"this is the first content",
#          "user_id":test_user["id"]},

#         {"title":"here is the second title",
#          "content":"this is the second content",
#          "user_id":test_user["id"]},

#         {"title":"here is the third title",
#          "content":"this is the third content",
#          "user_id":test_user["id"]},
#     ]
# session.add_all([
#     models.Post(title="here is the first title",content="this is the first content",user_id=test_user["id"]),
#     models.Post(title="here is the second title",content="this is the second content",user_id=test_user["id"]),
#     models.Post(title="here is the third title",content="this is the third content",user_id=test_user["id"]),

#     ])
# session.commit()
# session.query.all()