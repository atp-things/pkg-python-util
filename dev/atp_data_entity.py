# %%
import json
import atpthings as atp
import datetime as dt
import pandas as pd

from uuid import UUID

data_entity_new = {
    "type": "timeseries",
    "name": "dataEntityName",
    "description": "data entity description",
    "location": {"latdec": 45.9162927, "logdec": 14.2221454},
}


data_entity = atp.DataEntity()

# Create new
if True:
    data_entity.new(data_entity_new)


# Find one
if False:
    print(
        "Find DataFrame:",
        data_entity.find(
            {"type": "timeseries"},
            output=pd.DataFrame,
        ),
    )
    print(
        "Find dict:",
        data_entity.find(
            {"name": "dataEntityName"},
            output=dict,
        ),
    )

    print(
        "Find str:",
        data_entity.find(
            {"uuid": UUID("087d356f-9ace-4387-8145-2a15da152840")},
            output=str,
        ),
    )

# Delete
if False:
    data_entity.delete(UUID("087d356f-9ace-4387-8145-2a15da152840"))
