

from typing import Optional

from fastapi import FastAPI,HTTPException,status,Response
from fastapi.params import Body


from schemas import PostSchema




app=FastAPI()







from pydantic import BaseModel
# generate random id
from random import randrange


# database connection for postgres
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# while True:
try:
    connection=psycopg2.connect(
        host='localhost',
        database='social_DB',
        user='postgres',
        password='0000',
        cursor_factory=RealDictCursor, 
    )
    cursor=connection.cursor()
    print("database connection successs")
    # break
except Exception as error:
    print("database connection failed")
    print("the error is :",error) 
    # time.sleep(5)





@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(payload:PostSchema):
    # # dict() to convert the pydemic type to dictionary
    # payload_dict=payload.dict()
    # payload_dict["id"]=randrange(1,10000000)
    # my_posts.append(payload_dict)

    title=payload.title
    content=payload.content
    published=payload.published
    cursor.execute("insert into posts(title,content,published)values(%s,%s,%s) returning *",(title,content,published))
    new_post=cursor.fetchone()
    # cursor.execute(f"insert into posts(title,content,published) values({title},{content},{published})")
    
    connection.commit()
    
   
    return new_post


# get request



# get all posts
@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts=cursor.fetchall()

    print(posts)
    return posts





        

        
@app.get("/posts/{post_id}")
def get_post(post_id:int,response:Response):

    cursor.execute("select * from posts where id=%s",(str(post_id),))
    post=cursor.fetchone()

    # post= find_post(post_id)

    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"detail":"not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {post_id} is not found")
    print(post)
    return post






            
@app.delete("/posts/{post_id}")
def delete_post(post_id:int):

    cursor.execute("DELETE FROM posts WHERE id=%s RETURNING *",(str(post_id),))
    delete_post=cursor.fetchone()
    connection.commit()

    if delete_post==None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"the post with id: {post_id} is not found")

 
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# update post
@app.put("/posts/{post_id}")
def update_post(post_id:int,post:PostSchema):
    print(post)

    cursor.execute("update posts set title=%s,content=%s,published=%s where id=%s returning *",(post.title,post.content,post.published,str(post_id),))
    updated_post=cursor.fetchone()
    connection.commit()
    
    if updated_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with {post_id} is not found")

    return updated_post
    


    