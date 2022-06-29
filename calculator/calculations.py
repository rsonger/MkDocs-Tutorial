# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: The first number in the subtraction operation.
        b: The second number to be subtracted from the first.

    Returns:
        A number representing the difference of `a` and `b`.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: The first number of the multiplication operation.
        b: The second number of the multiplication operation.

    Returns:
        A number representing the product of `a` and `b`.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
    >>> divide(4.0, 2.0)
    2.0
    >>> divide(4, 2)
    2.0

    Args:
        a: The dividend in the division operation.
        b: The divisor in the division operation.

    Raises:
        ZeroDivisionError: The divisor is 0 making the result undefined.

    Returns:
        A number representing the arithmetic quotient of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)