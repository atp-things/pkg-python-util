"""
atpthings
=========

ATP Things python package

"""
from . import dict
from . import util
from .database.data_entity import DataEntity
from .database.data_timeseries import DataTimeseries

from . import _version

__version__ = _version.get_versions()["version"]
