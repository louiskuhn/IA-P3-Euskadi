from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'date':'01/01/2000'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, v: int = 1):
    return {
        'id': id,
        'blog_info': blog,
        'version' : v
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: str = Query(None,
                               title='Title of comment',
                               desciption='description of the comment',
                               alias='commentTitle',
                               deprecated=True),
    content: str = Body(
        ...,
        min_length=10,
        max_length=40,
        regex="^[a-z\s]*$"
        ),
    comment_id: int = Path(le=5),
    v : Optional[List[str]] = Query(['1.0', '1.1'])
    ):
    return {
            'id': id,
            'blog_info': blog,
            'comment_title': comment_title,
            'comment_id': comment_id,
            'content': content,
            'v': v
            }