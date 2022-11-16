from fastapi import FastAPI,Response,status,HTTPException,Depends
#from fastapi.params import Body

#import psycopg2
#import time
from sqlalchemy.orm import Session
#from psycopg2.extras import RealDictCursor
from .database import engine  #get_db
from . import models    #,schemas,utility
#from typing import List
from .routers import blogs,users,authentication,votes
from .config import settings

from fastapi.middleware.cors import CORSMiddleware







models.Base.metadata.create_all(engine)



app=FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)







#try:
    #conn=psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="Mighty1234",cursor_factory=RealDictCursor)
   # cursor=conn.cursor()
  #  print("database connection was successful")
    
#   print("there was a mistake with connection")
 #   print("Error",error)
   # time.sleep(2)



app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(votes.router)









#@app.post("/post")
#def all_post(post:schemas.Postcreate):
  #  cursor.execute("""INSERT INTO posts (title,contents,published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.contents,post.published))
 #   all_post=cursor.fetchall()
  #  conn.commit()

  #  return all_post


#@app.get('/post123')
#def get_all():
 #   cursor.execute("""SELECT * FROM posts""")
  #  get_all=cursor.fetchall()
   # return get_all







#@app.get("/post123/{id}")
#def get_one(id:str):
 #   cursor.execute("""SELECT * FROM posts WHERE  id= %s """, (str(id)))
  #  post=cursor.fetchone()
   # if not post:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'the {id} does not exit')
    #return post

#@app.delete("/post123/{id}")
#def delete(id:str):
    
   # cursor.execute("""DELETE FROM posts WHERE id= %s RETURNING * """, str((id),))
   # delete=cursor.fetchone()
   # conn.commit()
   # if delete==None:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'the {id} does not exit')
    #return Response(status_code=status.HTTP_404_NOT_FOUND)

    
#@app.put("/post123/{id}")
#def update(id:int,post:schemas.Postcreate):
 #   cursor.execute("""UPDATE posts SET title=%s , contents=%s, published=%s  WHERE id =%s RETURNING * """,(post.title,post.contents,post.published,str(id))  )  
  #  update =cursor.fetchone()
   # conn.commit()
   # if update==None:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'the {id} does not exit')
    #return {"data":update}

    