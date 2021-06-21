from collections.abc import Callable

fnc_counter_dict = {}


def fnc_counter() -> Callable:
    """
    This closure takes a function and counts how many times it has been executed
    Input: The function whose docstring length has to be checked.
    Output: The function that does the comparison
    """

    def inc(fn: Callable, *args, **kwargs) -> Callable:
        """
        Input: The function whose execution has to be counted, and its (compulsory arguments).
        Output: The function that does the counting
        """

        fnc_counter_dict[fn.__name__] = fnc_counter_dict.get(
            fn.__name__, 0) + 1
        return fn(*args, **kwargs)

    return inc


def add(x: int, y: int) -> int:
    """ A function that adds; The number of times this function has been called will be reported """
    return x + y


def mul(x: int, y: int) -> int:
    """ A function that multiplies; The number of times this function has been called will be reported """
    return x * y


def div(x: int, y: int) -> int:
    """ A function that divides; The number of times this function has been called will be reported """
    return x / y


counter = fnc_counter()
counter(add, 1, 2)
counter(add, 1, 2)
counter(add, 1, 2)

counter(mul, 1, 2)
counter(mul, 1, 2)
counter(mul, 1, 2)
counter(mul, 1, 2)

counter(div, 2, 1)
counter(div, 2, 1)
counter(div, 2, 1)
counter(div, 2, 1)
counter(div, 2, 1)


for key in fnc_counter_dict:
    print(f'The function {key} has been called {fnc_counter_dict[key]} times')
