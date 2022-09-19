# %% Dict
import json
import datetime as dt
import atpthings as atp

from uuid import UUID


dict_in = {"one": 1, "two": 2, "three": 3}
keys_list = ["one", "three"]
# %% get keys
print("get_keys")
print("Dict_in:", dict_in)
print("Dict_out:", atp.dict.get_keys(dict_in, keys_list))

# %% get values
print("get_values")
print("Dict_in:", dict_in)
print("Dict_out:", atp.dict.get_values(dict_in, keys_list))


# %% Convert list of dictionaries to dictionary by key.
dict_list = [
    {"name": "first_dict", "two": 2, "three": 3},
    {"name": "second_dict", "two": 5, "three": 8},
    {"name": "third_dict", "two": 3, "three": 356},
    {"name": "forth_dict", "two": 2, "three": 343, "fout": "sdf"},
]

dict_from_list = atp.dict.list_to_dict(dict_list, "name")
print("Dict from list:", dict_from_list)
