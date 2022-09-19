import pytest
import atpthings as atp

dict_in = {"one": 1, "two": 2, "three": 3}
keys_list = ["one", "three"]


def test_dict_get_keys():
    ret = {"one": 1, "three": 3}
    assert atp.dict.get_keys(dict_in, keys_list) == ret


def test_dict_get_values():
    ret = [1, 3]
    assert atp.dict.get_values(dict_in, keys_list) == ret
