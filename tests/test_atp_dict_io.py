import pytest
import atpthings as atp

dict_sample_001 = {"one": 1, "two": 2, "three": 3}


def test_dict_load():
    assert atp.dict.load("data_samples/dict_sample_001.json") == dict_sample_001


def test_dict_save():
    atp.dict.save(dict_sample_001, "tests/tmp/dict_sample_001.json")
    assert atp.dict.load("tests/tmp/dict_sample_001.json") == dict_sample_001
