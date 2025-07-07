import time
import functools
import signal

def raise_timeout(*args, **kwargs):
    raise TimeoutError()

signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

def timeout(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.alarm(n)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(5)
def foo():
    time.sleep(10)
    print('foo')

foo()
