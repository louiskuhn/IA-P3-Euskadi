from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True)
  email = Column(String, unique=True)
  password = Column(String)
  items = relationship('DbArticle', back_populates='user')

class DbArticle(Base):
  __tablename__= 'articles'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  published = Column(Boolean)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("DbUser", back_populates='items')