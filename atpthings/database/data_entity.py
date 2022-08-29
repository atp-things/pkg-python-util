"""
atpthings.database.data_entity
-------------------------
"""
from __future__ import annotations

import os
import json
import typing
import pandas as pd

from uuid import uuid4, UUID
from pymongo import MongoClient
from bson.json_util import dumps

old_default = json.JSONEncoder.default


def new_default(self, obj):
    if isinstance(obj, UUID):
        return str(obj)
    return old_default(self, obj)


json.JSONEncoder.default = new_default


def data_to_df(data):
    return pd.DataFrame(data)


def data_to_dict(data):
    return data


def data_to_str(data):
    return json.loads(json.dumps(data, default=str))


class DataEntity:
    def __init__(self, uri: str = None, user: str = None, password: str = None) -> None:
        self.uri = uri
        self.user = user
        self.password = password
        self.database = "entities"
        self.collection = "data"

        if self.uri is None:
            self.uri = os.getenv("MONGODB_ATP_CLOUD_URI")
        if self.user is None:
            self.user = os.getenv("MONGODB_ATP_CLOUD_USER")
        if self.password is None:
            self.password = os.getenv("MONGODB_ATP_CLOUD_PASSWORD")

        self.connect()
        pass

    def connect(self):
        self.db_client = MongoClient(
            self.uri,
            username=self.user,
            password=self.password,
            uuidRepresentation="standard",
        )
        self.data_entity_collection = self.db_client[self.database][self.collection]
        return self

    def new(self, data: dict):
        data["type"]
        data["uuid"] = uuid4()
        return self.data_entity_collection.insert_one(data)

    def find(
        self,
        *args: typing.Any,
        projection: dict = {"_id": False},
        output: pd.DataFrame | dict | str = None,
        **kwargs: typing.Any,
    ):
        ret = self.data_entity_collection.find(*args, projection, **kwargs)
        data = list(ret)

        if output == pd.DataFrame:
            return data_to_df(data)
        elif output == dict:
            return data_to_dict(data)
        elif output == str:
            return data_to_str(data)
        else:
            return ret

    def delete(self, uuid: UUID):
        filter: dict = {"uuid": uuid}
        return self.data_entity_collection.delete_one(filter)
