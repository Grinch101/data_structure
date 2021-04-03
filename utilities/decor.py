def timeit(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print('ended in', end - start)
        return output

    return wrapper

