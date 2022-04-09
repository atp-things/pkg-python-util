"""
atpthings.util.dictionary
-------------------------
"""


def getKeys(dictionary: dict, keys: list) -> dict:
    """Get keys from dictionary.

    Parameters
    ----------
    dictionary : dict
        Dictionary.
    keys : list
        List of keys wonted to be extracted.

    Returns
    -------
    dict
        Dictionry wit only specificated keys.

    Examples
    --------

    >>> dict1 = {"one": 1, "two": 1,"three": 1}
    >>> keysList = ["one", "three"]
    >>> dict2 = atpthings.util.dictionary.getKeys(dict1,keysList)
    >>> {"one": 1,"three": 1}
    """
    return {key: dictionary[key] for key in dictionary.keys() & keys}
