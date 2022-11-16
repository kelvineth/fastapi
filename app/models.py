from sqlalchemy import Integer,Column,Boolean,String,ForeignKey
from .database import Base
from sqlalchemy.sql.expression import null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__='posts'


    id=Column(Integer,primary_key=True,nullable=False)
    content=Column(String,nullable=False)
    title=Column(String,nullable=False)
    published=Column(Boolean,server_default='True',nullable=False )
    created=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner=relationship("User")


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    created=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))



class Votes(Base):
    __tablename__= "votes"
    posts_id=Column(Integer,ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)
    users_id=Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),primary_key=True)
    
    