
class Prime(object):

    def __init__(self, limit):
        self.limit = limit

    def generate_primes(self):
        primes = []
        range_limit = self.limit

        for num in range(2, range_limit):
            i = 2
            if num == 2:
                primes.append(num) 
            while i < num:
                if i <= (num / 2):
                    if num % i == 0:
                        break
                else:
                    primes.append(num) 
                    break
                i += 1

        return primes

# This is just a convention
if __name__ == '__main__':
    prime = Prime(100)
    print prime.generate_primes()
