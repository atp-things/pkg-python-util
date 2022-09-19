import pytest
import atpthings as atp


def test_dict_dict_to_list():
    dict_list = [
        {"name": "first_dict", "two": 2, "three": 3},
        {"name": "second_dict", "two": 5, "three": 8},
        {"name": "third_dict", "two": 3, "three": 356},
        {"name": "forth_dict", "two": 2, "three": 343, "fout": "sdf"},
    ]
    ret = {
        "first_dict": {"name": "first_dict", "two": 2, "three": 3},
        "second_dict": {"name": "second_dict", "two": 5, "three": 8},
        "third_dict": {"name": "third_dict", "two": 3, "three": 356},
        "forth_dict": {"name": "forth_dict", "two": 2, "three": 343, "fout": "sdf"},
    }

    assert atp.dict.list_to_dict(dict_list, "name") == ret
