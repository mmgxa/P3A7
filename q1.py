from collections.abc import Callable


def chk_docstr() -> Callable:
    """
    This closure takes a function and checks whether it has sufficient number of characters in its docstring
    Input: The function whose docstring length has to be checked.
    Output: The function that does the comparison
    """

    # This is the free variable (and is designated as nonlocal inside the 'length' function)
    min_len = 50

    def length(fn: Callable):
        """
        This inner function compares the length of the docstring with the minimum length.
        Input: Function for which the docs has to be checked.
        Output: True if doc length > 50 else False
        """

        nonlocal min_len
        print(f'Min. length is {min_len}')
        if len(fn.__doc__) > min_len:
            print('This function meets the minimum docstring length criteria\n')
        else:
            print('This function does not meet the minimum docstring length criteria\n')

    return length


def adder(x: int, y: int) -> int:
    """ Function with a Shorter Docstring """
    return x + y


def summer(x: int, y: int) -> int:
    """ This function has a sufficent length of docstring as defined by the free variable and will be deemed as valid """
    return x + y


checker = chk_docstr()
checker(adder)
checker(summer)
