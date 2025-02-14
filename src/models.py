import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from eralchemy2 import render_er

Base = declarative_base()

Follower = Table(
    'followers', 
    Base.metadata, 
    Column('user_from_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    firstname = Column(String(200))
    lastname = Column(String(200))
    email = Column(String(300), nullable=False, unique=True)
    Follower =relationship("Follower", secondary='user_from_id')
    Follower =relationship("Follower", secondary='user_to_id')


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user = relationship('User', backref="User")


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(300))
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship('Post', backref="Post")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comments = relationship('Comment', backref="Post")
    post = relationship('User', secondary=User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
