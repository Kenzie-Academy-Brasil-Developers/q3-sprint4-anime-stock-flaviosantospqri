from flask import jsonify, request
from http import HTTPStatus
from app.models.animes_model import Animes

def get_animes():
    animes = Animes.get_all_animes()

    animes_keys = ["id", "anime", "released_date", "seasons"]
    
    animes_list = [dict(zip(animes_keys, anime)) for anime in animes]

    print(type(animes_list))

    return jsonify(animes_list), HTTPStatus.CREATED

def create_animes():
    data = request.get_json()

    anime = Animes(**data)

    register_anime = anime.create_animes_model()

    animes_keys = ["id", "anime", "released_date", "seasons"]
    register_anime = dict(zip(animes_keys, register_anime))

    return jsonify(register_anime), HTTPStatus.CREATED
def find_animes(id):
    return jsonify({'msg': 'encontrou um anime'}), HTTPStatus.OK

def delete_animes(id):
    return jsonify({'msg': 'Deletou um anime'}), HTTPStatus.OK

def patch_animes(id):
    return jsonify({'msg': 'Atualizado'}), HTTPStatus.OK