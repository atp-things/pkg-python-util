"""
atpthings.dict.convert
----------------------
"""


def list_to_dict(list_of_dict: list, key: str) -> dict:
    """Convert list of dictionaries to dictionary by key.

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
