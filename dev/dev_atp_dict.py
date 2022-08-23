# %%
import json


import datetime as dt
from uuid import UUID

import atpthings


dict_in = {"one": 1, "two": 2, "three": 3}
keys_list = ["one", "three"]

print("get_keys")
print("Dict_in:", dict_in)
print("Dict_out:", atpthings.util.dictionary.get_keys(dict_in, keys_list))


print("get_values")
print("Dict_in:", dict_in)
print("Dict_out:", atpthings.util.dictionary.get_values(dict_in, keys_list))

# %%
