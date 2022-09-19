"""
atpthings.dict.io
-----------------
"""
import json


# load
def load(path: str) -> dict:
    """Load dictionary from file.

    Parameters
    ----------
    path : str
        Path to file.

    Returns
    -------
    dict
        Dictionary
    """
    with open(path) as file_:
        ret = dict(json.load(file_))

    return ret


# save
def save(dict_: dict, path: str) -> None:
    """Save dictionary to file.

    Parameters
    ----------
    dict_ : dict
        Dictionary.
    path : str
        Path to file.
    """
    with open(path, "w", encoding="utf-8") as file_:
        json.dump(dict_, file_, ensure_ascii=False)

    return
