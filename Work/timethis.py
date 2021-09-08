import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}:{end-start:0.2f}')
        return r
    return wrapper

@timethis
def countdown(n):
    while n>0:
        n -=1

