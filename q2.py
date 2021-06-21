from collections.abc import Callable


def fib() -> Callable:
    """ This  returns the next number in the Fibonacci Series"""
    f = [1, 1]  # The free variable

    def next() -> int:
        """ This is the closure that actually returns the next number"""

        nonlocal f
        l = len(f)
        n = f[l-1] + f[l-2]
        f.append(n)
        return n
    return next


fib_fn = fib()
print(f'The next fib number is {fib_fn()}')

print(f'The next fib number is {fib_fn()}')

print(f'The next fib number is {fib_fn()}')

print(f'The next fib number is {fib_fn()}')

print(f'The next fib number is {fib_fn()}')

print(f'The next fib number is {fib_fn()}')
