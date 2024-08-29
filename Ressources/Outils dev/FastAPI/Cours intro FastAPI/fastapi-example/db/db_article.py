from exceptions import StoryException
from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleBase
from fastapi import HTTPException, status


def create_article(db: Session, request: ArticleBase):
  if request.content.startswith('Once upon a time'):
    raise StoryException('No fairytales please')
  new_article = DbArticle(
    title = request.title,
    content = request.content,
    published = request.published,
    user_id = request.creator_id
  )
  db.add(new_article)
  db.commit()
  db.refresh(new_article)
  return new_article

def get_article(db: Session, id: int):
  article = db.query(DbArticle).filter(DbArticle.id == id).first()
  if not article:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Article with id {id} not found')
  return article