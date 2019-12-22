import time
import random
from itertools import islice


def timeit(f):
    """Counts function run time"""
    def timed(*args, **kw):
        before = time.time()
        result = f(*args, **kw)
        after = time.time()

        print "Elapsed time: ", after - before
        return result
    return timed

@timeit
def get_primes(n=2, call_one_prime=False):
    """Creates a generator object, use eg. get_primes(1459, True) to check
    if 1459 is a prime number"""
    while True:
        i = 2
        if n == 2:
            yield n
        while i < n:
            if i <= (n / 2):
                if n % i == 0:
                    break
            else:
                yield n
                break
            i += 1
        n += 1
        if call_one_prime:
            break

if __name__ == '__main__':
    # Example uses
    print list(islice(get_primes(), 1))
    print list(islice(get_primes(), 100))
    print list(islice(get_primes(), 50, 250))
