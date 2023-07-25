from functools import wraps
import timeit

def avg_10times(func):
    @wraps(func)
    def wrapper(*args):
        times_10 = 0
        for _ in range(10):
            starttime = timeit.default_timer()
            func(*args)
            times_10 += timeit.default_timer() - starttime
        times_10 /= 10
        return func(*args), times_10
    return wrapper