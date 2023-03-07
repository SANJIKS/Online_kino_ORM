from peewee import IntegrityError, DoesNotExist
from app.models.posts.post_model import Genre
from app.models.basemodel import db
from app.schemas.genres import GenreCreateSchema, GenreAllSchema

@db
def create_genre(genre_in: GenreCreateSchema):
    try:
        genre = Genre.create(title=genre_in.title)
    except IntegrityError:
        print('Genre is already exsist')

@db
def get_genres():
    genres = [genre.title for genre in Genre.select()]
    return GenreAllSchema.from_orm(genres)





# @db
# def create_genre(title: str):
#     try:
#         obj = Genre.create(title=title)
#     except IntegrityError:
#         obj = 0
#     return obj



@db
def delete_genre(title: str):
    try:
        genre = Genre.get(title=title)
        # SELECT * FROM genre WHERE title = title
        genre.delete_instance()
    except DoesNotExist:
        return 0
    return 1

# @db
# def get_genres():
#     genres = Genre.select(Genre.title)
#     return GenreAllSchema.from_orm(genres)




# @db
# def get_genres():
#     return [genre.title for genre in Genre.select()]


