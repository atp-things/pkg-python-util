"""
atpthings.dict.get
------------------
"""


def get_keys(dict_: dict, keys: list) -> dict:
    """Get keys from dictionary.

    Parameters
    ----------
    dict_ : dict
        Dictionary.
    keys : list
        List of keys to be extracted.

    Returns
    -------
    dict
        Dictionary with only specificated keys.

    Examples
    --------

    >>> dict_in = {"one": 1, "two": 2, "three": 3}
    >>> keys_list = ["one", "three"]
    >>> atpthings.util.dictionary.get_keys(dict_in, keys_list)
    >>> {'one': 1, 'three': 3}
    """

    return {key: dict_[key] for key in dict_.keys() & keys}


def get_keys_as_list(dict_: dict) -> list:
    """Get keys from dictionary as list.

    Parameters
    ----------
    dict_ : dict
                Dictionary.

    Returns
    -------
    list
        List of all keys in dictionary (1. level).
    """
    return [key for key in dict_.keys()]


def get_values(dict_: dict, keys: list) -> list:
    """Get values of specific keys from dictionary to list.

    Parameters
    ----------
    dict_ : dict
        Dictionary.
    keys : list
        List of keys wonted to be extracted.

    Returns
    -------
    dict
        List of values with specificated key.

    Examples
    --------

    >>> dict_in = {"one": 1, "two": 2, "three": 3}
    >>> keys_list = ["one", "three"]
    >>> atpthings.util.dictionary.get_values(dict_in, keys_list)
    >>> [1, 3]
    """
    # TODO: support for None keys list -> return all values

    return [dict_[item] for item in keys]


# List of dicts
def get_values_from_dict_list(dict_list: list, key: str, unique: bool = False) -> list:
    """Get key values from list of dictionaries.

    Parameters
    ----------
    dict_list : list
        List of dictionaries
    key : str
        Key to be searched.
    unique : bool, optional (default False)
        Output uniques.

    Returns
    -------
    list
        List of key values.
    """
    # TODO: What to do if key is missing

    list_ = []
    for item in dict_list:
        list_.append(item[key])

    if unique:
        return list(set(list_))

    return list_
