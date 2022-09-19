# %% Dict input/output
import atpthings as atp

# %% Load dict

dict_1 = atp.dict.load("data_samples/dict_sample_001.json")
print("Dict:", dict_1)
atp.dict.save(dict_1, "dev/tmp/dict_sample_001.json")
dict_2 = atp.dict.load("dev/tmp/dict_sample_001.json")
print("Dict:", dict_2)
print("Dict equal:", dict_1 == dict_2)
