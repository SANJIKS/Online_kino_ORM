from app.queries.posts import (
    create_post,
    get_all_films,
    get_film_by_id
    )
from app.schemas.posts import  PostCreateSchema

from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films():
    return get_all_films()

# @router.get('/posts')
# def get_one_film(id):
#     return get_film_by_id(id)


@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)