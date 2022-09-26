# %% Dict input/output
import atpthings as atp

dict_1 = atp.dict.load("data_samples/dict_sample_001.json", file_type="json")
print("Dict load:", dict_1)
atp.dict.save(dict_1, "dev/tmp/dict_sample_001.json")

dict_2 = atp.dict.load("dev/tmp/dict_sample_001.json")
print("Dict save/load:", dict_2)
print("Dict equal:", dict_1 == dict_2)

atp.dict.save(dict_1, "dev/tmp/dict_sample_001.x_json", file_type="json")
print(
    "Dict save/load v2:",
    atp.dict.load("dev/tmp/dict_sample_001.x_json", file_type="json"),
)
