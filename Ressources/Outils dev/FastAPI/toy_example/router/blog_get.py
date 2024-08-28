from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.get(
        '/all',
        summary="Get all available blogs",
        description="API call that simulates getting all blogs",
        response_description="List of all blogs")
def get_all_blogs(page: int=1, page_size: Optional[int] = None):
    return {"msg": f"All {page_size} blogs on {page=}"}

@router.get("/{id}/comments/{comment_id}", tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, pseudo: Optional[str] = None):
    """
    Simulates getting one comment of a blog
    - **id** required path parameter
    - **comment_id** required path parameter
    - **valid** optional query parameter
    - **pseudo** optional query parameter
    """
    return {"msg": f"comment {comment_id} on blog {id} by {pseudo}, {valid}"}

class BlogType(str, Enum):
    short = "Short"
    story = "Story"
    howto = "Howto"

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {"msg": f"Blog {type=}"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error":f"Blog {id=} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"msg": f"Blog {id=}"}
