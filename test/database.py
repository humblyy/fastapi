

# from fastapi.testclient import TestClient
# from app.orm import app

# from app.database import get_db

# from sqlalchemy import create_engine

# from sqlalchemy.orm import sessionmaker
# from app import models
# import pytest


# # establish connection between database and sqlalchemy
# SQLALCHEMY_DATABASE_URL=f'postgresql://postgres:0000@localhost/test_social'
# engine=create_engine(SQLALCHEMY_DATABASE_URL)

# TestingsessionLocal=sessionmaker(autoflush=False,bind=engine,expire_on_commit=False)





# @pytest.fixture(scope="module")
# def session():
   
#     models.Base.metadata.drop_all(bind=engine)
#     # create the tables
#     models.Base.metadata.create_all(bind=engine)
#     db=TestingsessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()




# # create fixture to pass duplicate constriant
# @pytest.fixture(scope="module")
# def client(session):
#     def override_get_db():
        
#         try:
#             yield session
#         finally:
#             session.close()
#     app.dependency_overrides[get_db]=override_get_db
    
    
#     yield TestClient(app)