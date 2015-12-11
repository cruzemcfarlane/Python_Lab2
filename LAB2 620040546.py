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
    for count in range(2,n):  
       if (n%count == 0):     
        return False                                   
    return True
    
#Question 4
def primes(a,b):
    def isPrime(n):
        for count in range(2,n):
            if (n%count == 0):
                return False
        return True
    
    for counter in range(a,b):
        if isPrime(counter):
            print counter

