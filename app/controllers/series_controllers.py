from hashlib import new
from http import HTTPStatus
import imp
from app.models.series_models import Series
from flask import request
from psycopg2.errors import InvalidTextRepresentation
from psycopg2.errors import UniqueViolation

def create():
    data = request.get_json()

    new_data = Series(**data)

    try:
        data_request = Series.writer_series(new_data.__dict__)
    except InvalidTextRepresentation as e:
        text = str(e.args).split(":")[0].replace("(", "").replace("'", "")
        return {"error": text}, HTTPStatus.UNPROCESSABLE_ENTITY
    except UniqueViolation as e:
        text = str(e.args).split("=")[1].split(".")[0].replace("(", "").replace(")", "")
        return {"error": text}, HTTPStatus.UNPROCESSABLE_ENTITY

    fieldnames = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

    new_data_request = dict(zip(fieldnames, data_request))

    return {"data": new_data_request}, HTTPStatus.CREATED


def series():
    data = Series.reader_series()

    return {"data": data}, HTTPStatus.OK


def select_by_id(id):

    data = Series.reader_series_by_id(id)

    if not data:
        return {"msg": f"id {id} not found!"}, HTTPStatus.NOT_FOUND

    fieldnames = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

    data_new = dict(zip(fieldnames, data))
    return {"data": data_new}, HTTPStatus.OK