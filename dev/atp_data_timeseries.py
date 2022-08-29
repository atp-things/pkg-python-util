# %%
import json
import random
import atpthings as atp
import datetime as dt
import pandas as pd

from uuid import UUID

data_timeseries_new = {
    "uuid": UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c"),
    "ts": dt.datetime.utcnow(),
    "value": random.randint(0, 100),
}

data_timeseries_list_new = [
    {
        "uuid": UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c"),
        "ts": dt.datetime.utcnow(),
        "value": random.randint(0, 100),
    },
    {
        "uuid": UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c"),
        "ts": dt.datetime.utcnow(),
        "value": random.randint(0, 100),
    },
]


data_timeseries = atp.DataTimeseries()

# Insert
if False:
    data_timeseries.insert(data_timeseries_new)

# Insert list
if True:
    data_timeseries.insert(data_timeseries_list_new)

# TODO: Insert DataFrame
# if True:
#     data_timeseries.insert(data_timeseries_list_new)


# Find one
if True:
    print(
        "Find DataFrame:",
        data_timeseries.find(
            uuid=[UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c")],
            ts_from=dt.datetime(2022, 8, 29, 22, 20, 17, 609000),
            output=pd.DataFrame,
        ),
    )
    print(
        "Find dict:",
        data_timeseries.find(
            uuid=[UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c")],
            ts_from=dt.datetime(2022, 8, 29, 22, 18, 17, 609000),
            output=dict,
        ),
    )

    print(
        "Find str:",
        data_timeseries.find(
            uuid=[UUID("a27207c4-cdd3-44d5-8dec-1f3c9fed6d6c")],
            output=str,
        ),
    )

# Delete
if False:
    data_timeseries.delete(UUID("087d356f-9ace-4387-8145-2a15da152840"))
