from functools import wraps
import time


def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('=======================\n%r took %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


def timer(t):
    """
    Function decorator that enforces a time interval between function calls.
    """
    def wrapper(f):
        @wraps(f)
        def wrapped_func(*args, **kwargs):
            now = time.time()
            if now - wrapped_func.latest > t:
                f(*args, **kwargs)
                wrapped_func.latest = now
        wrapped_func.latest = time.time()
        return wrapped_func
    return wrapper
