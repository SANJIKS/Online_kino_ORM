from app.models.posts.post_model import Genre, Post, PostGenres
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.schemas.genres import GenreCreateSchema
from datetime import date
from app.routes.posts import router
from fastapi import FastAPI


app = FastAPI()


app.include_router(router)








# @db
# def create_tables() -> None:
#     db_connection.create_tables([Genre, Post, PostGenres])

