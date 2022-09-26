"""
atpthings.dict.io
-----------------
"""
from __future__ import annotations
from pathlib import Path
import json
import yaml

# Help: https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python


# load
def load(path: str, file_type: str = None) -> dict:
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

    if file_type is None:
        file_type = Path(path).suffix.split(".")[-1]

    match file_type.lower():
        case "json":
            return _load_json(path)
        case ("yml" | "yaml"):
            return _load_yml(path)
        case "ini":
            # import configparser
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "xml":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "pickle":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "env":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case _:
            raise Exception("File type not supported.")


def save(dict_: dict, path: str, file_type: str = None) -> None:
    """Save dictionary to file.

    Parameters
    ----------
    dict_ : dict
        Dictionary.
    path : str
        Path to file.
    """

    if file_type is None:
        file_type = Path(path).suffix.split(".")[-1]

    match file_type.lower():
        case "json":
            return _save_json(dict_, path)
        case ("yml" | "yaml"):
            return _save_yml(dict_, path)
        case "ini":
            # import configparser
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "xml":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "pickle":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case "env":
            raise Exception(f"File type ({file_type}) not supported yet.")
        case _:
            raise Exception(f"File type ({file_type}) not supported.")


# json
def _load_json(path: str) -> dict:
    with open(path) as file_:
        ret = dict(json.load(file_))

    return ret


def _save_json(dict_: dict, path: str) -> None:

    with open(path, "w", encoding="utf-8") as file_:
        json.dump(dict_, file_, ensure_ascii=False)

    return


# yml
def _load_yml(path: str) -> dict:
    with open(path, "r") as file_:
        return dict(yaml.safe_load(file_))


def _save_yml(dict_: dict, path: str) -> None:

    with open(path, "w", encoding="utf-8") as file_:
        return yaml.dump(dict_, file_, default_flow_style=False, allow_unicode=True)
