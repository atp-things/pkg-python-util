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
