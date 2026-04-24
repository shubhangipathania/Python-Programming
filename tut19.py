#docstrings in python
def multiply(a,b):
    '''THIS TAKES UP TWO INTEGERS AND RETURN THE PRODUCT OF THE TWO.'''
    result=a*b
    return result

c=multiply(45,2)
print(c)
print(multiply.__doc__)


def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

a=add(67,100)
print(a)
print(add.__doc__)

import this