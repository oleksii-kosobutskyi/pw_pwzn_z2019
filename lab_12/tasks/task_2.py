from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        fun_name = fun.__name__
        opt_param = ", ".join(kwargs.keys()) if kwargs else '-'
        time_elapsed = time()
        return_val = fun(*args, **kwargs)
        time_elapsed = time() - time_elapsed
        print(
            f"{timestamp}| function {fun_name} called with:\n"
            f"{len(args)} positional parameters\n"
            f"optional parameters: {opt_param}\n"
            f"returned: {return_val} ({time_elapsed:.2e}s)"
        )
    return wrapper


@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 positional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 positional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
