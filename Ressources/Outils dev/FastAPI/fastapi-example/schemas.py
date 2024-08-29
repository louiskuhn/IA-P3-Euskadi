from typing import List
from pydantic import BaseModel, ConfigDict

# Article inside UserDisplay
class Article(BaseModel):
  title: str
  content: str
  published: bool
  model_config = ConfigDict(from_attributes = True)

# User data retrieved from client
class UserBase(BaseModel):
  username: str
  email: str
  password: str

# User data for the response
class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Article] = []
  model_config = ConfigDict(from_attributes = True)

# User inside ArticleDisplay
class User(BaseModel):
  id: int
  username: str
  model_config = ConfigDict(from_attributes = True)

# Article data retrieved from client
class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

# Article data for the response
class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User
  model_config = ConfigDict(from_attributes = True)