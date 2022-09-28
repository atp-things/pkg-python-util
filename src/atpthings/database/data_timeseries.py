"""
atpthings.database.data_entity
-------------------------
"""
from __future__ import annotations

import os
import json
import typing
import pandas as pd
import datetime as dt

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


def data_to_df_ts(data):
    df = pd.DataFrame(data)
    try:
        df.set_index("ts", inplace=True)
        pass
    except Exception:
        pass
    return df


def data_to_dict(data):
    return data


def data_to_str(data):
    return json.loads(json.dumps(data, default=str))


class DataTimeseries:
    def __init__(self, uri: str = None, user: str = None, password: str = None) -> None:
        self.uri = uri
        self.user = user
        self.password = password
        self.database = "entities"
        self.collection = "timeseries"

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
        self.data_timeseries_collection = self.db_client[self.database][self.collection]
        return self

    def insert(self, data: dict | list | pd.DataFrame):
        if type(data) == dict:
            data["ts"]
            data["uuid"]
            return self.data_timeseries_collection.insert_one(data)
        elif type(data) == list:
            # TODO: check for "ts" and "uuid"
            return self.data_timeseries_collection.insert_many(data)
        elif type(data) == pd.DataFrame:
            # check for colum names
            df = data.copy()  # check if this is needed
            df.reset_index(inplace=True)
            document = df.to_dict("records")
            return self.data_timeseries_collection.insert_many(document)

    def find(
        self,
        uuid: UUID | list(UUID),
        ts_from: dt.datetime = None,
        ts_to: dt.datetime = None,
        output: pd.DataFrame | dict | str = None,
    ):
        if type(uuid) == UUID:
            list(uuid)

        filter: dict = {"$and": [{"uuid": {"$in": uuid}}]}

        if ts_from:
            filter["$and"].append({"ts": {"$gte": ts_from}})

        if ts_to:
            filter["$and"].append({"ts": {"$lte": ts_to}})

        ret = self.data_timeseries_collection.find(
            filter=filter,
            projection={
                "_id": 0,
            },
        )
        data = list(ret)

        if output == pd.DataFrame:
            return data_to_df_ts(data)
        elif output == dict:
            return data_to_dict(data)
        elif output == str:
            return data_to_str(data)
        else:
            return ret

    def delete(self, uuid: UUID):
        return self.data_timeseries_collection.delete_many({"uuid": uuid})
