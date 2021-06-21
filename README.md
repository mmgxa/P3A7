# P3A7

Note: Helper functions and imports are not shown in the following code segments!

The questions in the assignments are related to Closures - nested function with a free variable(s). For 

**Q1: Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable**  

Note that the question requires that the minimum length is stored as a free variable - `min_len` in the following case.


```python
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
```

**Q2: Write a closure that gives you the next Fibonacci number**  

For the first two runs, the number 1 will be reported, followed by 2, 3, 5, etc.

```python
def fib() -> Callable:
    """ This  returns the next number in the Fibonacci Series"""
    f = []  # The free variable

    def next() -> int:
        """ This is the closure that actually returns the next number"""

        nonlocal f
        l = len(f)
        if l == 0 or l == 1:
            n = 1
        else:
            n = f[l-1] + f[l-2]
        f.append(n)
        return n
    return next
```

**Q3: We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts**  

Here, the `fnc_counter_dict` is the global dictionary variable and stores the count

```python
fnc_counter_dict = {} # global dictionary variable

def fnc_counter() -> Callable:
    """
    This closure takes a function and counts how many times it has been executed
    Output: The function that does the counting
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
```

**Q4: Modify above such that now we can pass in different dictionary variables to update different dictionaries**

Three difference dictionaries (assuming three different functions) are delared as global variables and passed to the function

```python
add_counter_dict = {}
mul_counter_dict = {}
div_counter_dict = {}

def fnc_counter(fnc_counter_dict: dict) -> Callable:
    """
    This closure takes a function and counts how many times it has been executed
    Input: The dictionary where the count has to be stored.
    Output: The function that does the comparison
    """
    def inc(fn: Callable, *args, **kwargs) -> Callable:

        fnc_counter_dict['count'] = fnc_counter_dict.get('count', 0) + 1
        return fn(*args, **kwargs)

    return inc
```

    
