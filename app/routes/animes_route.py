from flask import Blueprint

from app.controllers import animes_controller

bp = Blueprint('delete_anime', __name__,)

@bp.delete('/animes/<int:anime_id>')
def delete_anime(anime_id):
    ...

@bp.get('/animes/<int:anime_id>')
def get_anime_id(anime_id):
     ...

@bp.get('/animes')
def get_animes():
    return animes_controller.get_animes()

@bp.patch('/animes/<int:anime_id>')
def update_anime(anime_id):
    ...

@bp.post('/animes')
def create_anime():
    return animes_controller.create_animes()