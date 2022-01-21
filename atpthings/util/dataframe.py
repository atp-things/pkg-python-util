"""
ATPthings: Pandas.DataFrame
---------------------------------
"""


def add_one(number: int = 8) -> int:
    """Add one

    :param number: write number
    :type number: int
    :return: return the number
    :rtype: int
    """

    return number + 1


def add_two(number: int) -> int:
    """Add two

    :param number: write number
    :type number: int
    :return: return the number
    :rtype: int
    """

    return number + 2


def add_sum(number1: int, number2: int, number3: int = 6) -> int:
    """Sum

    Sum all three numbers

    Parameters
    ----------
    number1:
        Number one.

    number2:
        Number two.

    number3:
        Number three.

    Returns
    -------
        N arrays with N dimensions each, with N the number of input
        sequences. Together these arrays form an open mesh.

    See Also
    --------
    add_two

    Notes
    -----
    This is really just `rfftn` with different default behavior.
    For more details see `rfftn`.

    Examples
    --------
    >>> import texthero as hero
    >>> import pandas as pd
    >>> s = pd.Series("1234 falcon9")
    >>> hero.preprocessing.replace_digits(s, "X")
    0    X falcon9
    dtype: object
    >>> hero.preprocessing.replace_digits(s, "X", only_blocks=False)
    0    X falconX
    dtype: object

    >>> import texthero as hero
    >>> import pandas as pd
    >>> s = pd.Series("1234 falcon9")
    >>> hero.preprocessing.replace_digits(s, "X")
    """

    return number1 + number2 + number3
