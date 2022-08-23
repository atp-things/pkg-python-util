"""
atpthings.util.dictionary
-------------------------
"""
import json

# manipulation


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

    return [dict_[key] for key in dict_.keys() & keys]


# list of dict
def convert_list_to_dict(list_of_dict: list, key: str) -> dict:
    """Convert List of dictionaries to dictionary.

    Parameters
    ----------
    list_of_dict : list
        List of dictionaries.
    key : str
        Key which value will be used for primary key of dict.

    Returns
    -------
    dict
        Dictionary created from list of dictionaries.
    """
    dict_ = {}
    duplicates_counter = 0
    for item in list_of_dict:
        key_name = item[key]
        if key_name in dict_:
            key_name = f"{key_name}_{duplicates_counter}"
            duplicates_counter += 1
        dict_[key_name] = item

    return dict_


# load


def load(path: str) -> dict:
    with open(path) as file_:
        ret = dict(json.load(file_))

    return ret


# save
