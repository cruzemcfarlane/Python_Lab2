#Question 1
def quadratic(a,b,c):
    discriminant=b**2-4*a*c
    if discriminant>0:
        root1 = ((-b+((b**2-4*a*c)**.5))/(2*a*c))
        root2 = ((-b-((b**2-4*a*c)**.5))/(2*a*c))
        
        if root1>root2:
            return root2
        else:
            return root1
    else:
        print 'No real roots'

#Question 2
def check_fermat(a,b,c,n):
    if n>2:
        print 'I made a discovery - Fermat was wrong'
        return False
    elif n<=0:
        print 'Error'
    elif c**n==a**n+b**n:
        return True
    else:
        return False

#Question 3
def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n%x==0:
            return False
    return True
    

def primes(a,b):
    def isPrime(n):
        if n<2:
            return False
        elif n==2:
            return True
        elif n%2==0:
            return False
    for counter in range(a,b):
        if isPrime(counter):
            print counter
    
"""
        if n>1:
            for count in range(2,n):
                if n%count==0 or n==0 or count==1:
                    return False
                return True

    for counter in range(a,b):
        if isPrime(counter):
            print counter

"""

























# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
#Question 4
def primes2(a,b):
    def isPrime(n):
        if n>1:
            for i in range(2,n):
                if n%i==0 or i==1 or n==0:
                    return False
            return True
        
        return False
    
    for i in range (a,b):
        if isPrime(i):
                print i
