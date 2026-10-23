


from fastapi import FastAPI

# db connection for alchemy

from . import models  
from .database import engine

from routes import userRoutes,postRoutes,authRoutes,voteRoutes

from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy to connect to the database and create all the tables and columns when the app starts if alembic is used this one is not needed
models.Base.metadata.create_all(bind=engine)

app=FastAPI()
# add cors middleware
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)


app.include_router(postRoutes.router)
app.include_router(userRoutes.router)
app.include_router(authRoutes.router)
app.include_router(voteRoutes.router)



    


