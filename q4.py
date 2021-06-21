from collections.abc import Callable

add_counter_dict = {}
mul_counter_dict = {}
div_counter_dict = {}


def fnc_counter(fnc_counter_dict: dict) -> Callable:

    def inc(fn: Callable, *args, **kwargs) -> Callable:

        fnc_counter_dict['count'] = fnc_counter_dict.get('count', 0) + 1
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


counter_add = fnc_counter(add_counter_dict)
counter_mul = fnc_counter(mul_counter_dict)
counter_div = fnc_counter(div_counter_dict)


counter_add(add, 1, 2)
counter_add(add, 1, 2)
counter_add(add, 1, 2)

counter_mul(mul, 1, 2)
counter_mul(mul, 1, 2)
counter_mul(mul, 1, 2)
counter_mul(mul, 1, 2)


counter_div(div, 2, 1)
counter_div(div, 2, 1)
counter_div(div, 2, 1)
counter_div(div, 2, 1)
counter_div(div, 2, 1)


def print_count(fn):
    fn_dict = globals()[fn.__name__ + '_counter_dict']
    print(
        f'The function {fn.__name__} has been called {fn_dict["count"]} time')


print_count(add)
print_count(mul)
print_count(div)
