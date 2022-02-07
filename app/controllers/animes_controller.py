from flask import jsonify, request
from http import HTTPStatus
from app.models.animes_model import Animes
from psycopg2.errors import UniqueViolation


available_keys = ['anime', 'released_date', 'seasons']

def get_animes():

    try:
        animes = Animes.get_all_animes()


        animes_list = Animes.serialize_method(animes)

        return jsonify(animes_list), HTTPStatus.OK
    except:
        return {'msg': 'Error'}, HTTPStatus.BAD_GATEWAY


def create_animes():
   
    try:
        data = request.get_json()

        anime = Animes(**data)

        register_anime = anime.create_animes_model()
        
    except KeyError:
        data_keys = list(data.keys())
        keys_erro = set(data_keys) - set(available_keys) 
        return jsonify({'available_keys': f'expected {available_keys}, received {keys_erro}' }), HTTPStatus.UNPROCESSABLE_ENTITY
    except UniqueViolation:
        return {'msg':'Anime already exists'}, HTTPStatus.CONFLICT

    register_anime = Animes.serialize_method(register_anime)

    return jsonify(register_anime), HTTPStatus.CREATED
    
def update_animes(id):
    try:
        data = request.get_json()

        update_anime = Animes.patch_animes(id, payload=data)

        if not update_anime:
           return {'msg': 'id não encontrado'}, HTTPStatus.NOT_FOUND
    except:
        data_keys = list(data.keys())
        keys_erro = set(data_keys) - set(available_keys) 
        return jsonify({'available_keys': f'expected {available_keys}, received {keys_erro}'}), HTTPStatus.UNPROCESSABLE_ENTITY

       
    serializer_anime = Animes.serialize_method(update_anime)
        
    return jsonify(serializer_anime), HTTPStatus.ACCEPTED
    

def delete_animes(id):
    deleted_anime = Animes.delete_animes(id)

    if not deleted_anime:
        return {'msg': 'id não encontrado'}, HTTPStatus.NOT_FOUND
        
    serializer_anime = Animes.serialize_method(deleted_anime)
    
    return jsonify(serializer_anime), HTTPStatus.ACCEPTED

def find_anime(id):
    finded_anime = Animes.find_anime(id)

    if not finded_anime:
        return {'msg': 'id não encontrado'}, HTTPStatus.NOT_FOUND
        
    serializer_anime = Animes.serialize_method(finded_anime)
    
    return jsonify(serializer_anime), HTTPStatus.ACCEPTED
