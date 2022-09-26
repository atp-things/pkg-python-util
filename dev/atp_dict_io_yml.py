# %% Dict input/output
import atpthings as atp
import os

# %% Load dict


dict_1 = atp.dict.load("data_samples/dict_sample_001.yml", file_type="yAml")
print("Dict load:", dict_1)
atp.dict.save(dict_1, "dev/tmp/dict_sample_001.yml")
dict_2 = atp.dict.load("dev/tmp/dict_sample_001.yml")
print("Dict save/load:", dict_2)
print("Dict equal:", dict_1 == dict_2)

atp.dict.save(dict_1, "dev/tmp/dict_sample_001.x_yml", file_type="yml")
print(
    "Dict save/load v2:",
    atp.dict.load("dev/tmp/dict_sample_001.x_yml", file_type="yml"),
)
