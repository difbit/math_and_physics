
import time


class Prime(object):

    def __init__(self, limit):
        self.limit = limit

    def timeit(f):
        def timed(*args, **kw):
            before = time.time()
            result = f(*args, **kw)
            after = time.time()

            print "Elapsed time: ", after - before
            return result
        return timed

    @timeit
    def get_primes(self):
        range_limit = self.limit

        for num in range(2, range_limit):
            i = 2
            if num == 2:
                yield num
            while i < num:
                if i <= (num / 2):
                    if num % i == 0:
                        break
                else:
                    yield num
                    break
                i += 1

if __name__ == '__main__':
    prime = Prime(10000000)
    print prime.get_primes()
