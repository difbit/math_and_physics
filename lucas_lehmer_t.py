import time
import sys

"""
This is a simple python program to check
if a Mersenne number 2^p-1 is a prime
number. The program asks the user to give
a prime number p and starts computing
after that.
"""

class Question(object):

    def __init__(self, p):
        self.p = p

    def ask(self):
        self.p = raw_input('\nGive a prime number: ')
        self.p = int(self.p)
        if self.p == 0:
            print "\nExiting.."
            exit()
        elif self.p <= 1:
            print "\nPlease give a positive number that is bigger than 1"
            print "___________________________________________________"
            self.ask()
        elif not self.is_the_given_number_prime():#self.p not in prime_list:
            print "\np must be prime \n"
            #print "A list for some small prime numbers: %r\n" % prime_list
            for_test.ask()
        # A limit can be used if wanted
        #elif self.p > 10000:
        #    print "This number is too big for this program"
        #    for_test.ask()
        else:
            return self.p

    def is_the_given_number_prime(self):
        """Check if given number is a prime number"""
        for number in range(2, self.p):
            #sample = self.p % number
            if self.p % number == 0:
                return False
        return True

    # Make prime number list
    # Might be used later to showcase a prime number list
    def generate_prime_list(self):
        list = range(1, 1001)
        composite = []
        for a in range(2, 501):
            for b in range(2, 501):
                composite.append(a*b)

        prime_list = [x for x in list if x not in composite]

def lucas_lehmer_prime_test(p):
    if p == 2 or p == 3:
        print "\nMersenne number 2^%r-1 is a prime number!" % p
        print "________________________________________\n"
        return
    # M is Mersenne number
    M = 2**p - 1
    i = 1
    # s is given a starting value 4
    s = 4
    #######
    # Loops p - 2 times while increasing s.
    # This s is an important number, since M has to divide s^2-2 for
    # M to be a prime number. This has been proved to be 100% accurate,
    # meaning that if M divides s[p-1] with zero residue then M is
    # definitely a prime number!
    #######
    while (i - 1) <= p - 2:
        s = (i*s)**2 - 2
        j = 0
        while (j - 1) <= p - 2:
            # Loops around residue s unless it is zero or j-1 reaches p-2
            s = ((s * s) - 2) % M
            j += 1
            if s == 0:
                print "\nMersenne number 2^%r-1 is a prime number!" % p
                print "________________________________________\n"
                return
        i += 1
    print "\nThe number 2^%r-1 is not prime\n" % p
    print "******************************\n"

if __name__ == '__main__':
    print "Quit program by writing 0\n"
    while True:
        for_test = Question(0)
        for_test.ask()
        toc = time.clock()
        lucas_lehmer_prime_test(for_test.p)
        tac = time.clock()
        print "Time spent:", tac - toc
