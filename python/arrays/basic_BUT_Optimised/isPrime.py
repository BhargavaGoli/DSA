def isPrime(n) :
    
    if n <= 1 : return False
    if n == 2 or n == 3 : return True
    if n % 2 == 0 and n % 3 == 0 : return False

    for i in range(5,int(n ** 0.5) + 1, 6) :
        if n % i == 0 or n & (i + 2) == 0 :
            return False
        
    return True

n = int(input("Enter the number"))
print(isPrime(n))