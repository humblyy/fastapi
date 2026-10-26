

# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

# SQLALCHEMY_DATABASE_URL='postgresql://postgres:0000@localhost/socialapp'



from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.envConfig import settings
# from .envConfig import settings

# establish connection between database and sqlalchemy
SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.database_hostname}/{settings.database_name}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal=sessionmaker(autoflush=False,bind=engine,expire_on_commit=False)
Base=declarative_base()

# db connection for alchemy
# create dependancy
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()