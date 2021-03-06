import math 

def isprime(n):
    """(int) -> boolean

    Take an int and test if the int is prime, return a boolean indication

    >>> isprime(2)
    True
    >>> isprime(999)
    False
    """

    m = int(math.floor(n**0.5) + 1)
    
    for i in range(2, m):
        #print('n:', n, 'i:', i, 'n%i:', n%i, 'm;', m)
        if (n % i) == 0:
            return False
    return True


def prime(low, high):
    """ (int, int) -> list of int

    Test which inteters between low and high are prime ints and return
    a list on prime integers, low should not be lower than 2

    >>>prime(2, 10)
    [2, 3, 5, 7]
    >>>prime(10, 20)
    [11, 13, 17, 19]
    """

    if low < 2:
        low = 2
    
    primes = []
    for i in range(low, high):
        if i % 2 == 0:
            continue
        else:
            if isprime(i):
                primes.append(i)
                
    return primes


def ispalindroom(n):
    """ (int) -> boolean
    
    Function takes an int determines if the int is a palindroom and returns
    a boolean indication

    >>> ispalindroom(11)
    True
    >>> ispalindroom(1011)
    False
    """
    
    half_num_num = int((math.log10(n) + 1) // 2)
    n = str(n)
    test = False
    
    for i in range((half_num_num)):
        if n[i] == n[-(i + 1)]:
            test = True
        else:
            return False

    return test


def palindroom(low, high):
    """ (int, int) -> list of int

    Determines the palindrome ints found between the low and high ints and
    returns a list of these ints

    >>> palindrm(10, 100)
    [11, 22, 33, 44, 55, 66, 77, 88, 99]
    >>> palindrm(100, 155)
    [101, 111]
    """

    palindrm = []
    
    for i in range(low, high):
        if ispalindroom(i):
            palindrm.append(i)


    return palindrm
            
    
def palindrooms_prime(low, high):
    """ (int, int) -> list of int

    Determine which palindrooms numbers in the range low and high are
    prime numbers
    
    >>> palindrooms_first(2, 112)
    [11, 101]
    """

    if low < 11:
        low = 11
        
    p = palindroom(low, high)
    palindrooms_prime = []

    for i in range(len(p)):
        if isprime(p[i]):
            palindrooms_prime.append(p[i])

    return palindrooms_prime
    
def prime_palindrooms(low, high):
    """ (int, int) -> list of int

    Determine which prime numbers in the range low and high are
    palindrooms

    >>> palindroom(2 20)
    [11]
    """
    
    if low < 11:
        low = 11
        
    primes = prime(low, high)
    palindrooms = []
    
    for i in range(len(primes)):
        if ispalindroom(primes[i]):
            palindrooms.append(primes[i])

    return palindrooms

if __name__ == '__main__':
    # print(prime_palindrooms(1, 100000))
    for b in palindrooms_prime(100000000, 1000000000):
        print b
    # print len(a)