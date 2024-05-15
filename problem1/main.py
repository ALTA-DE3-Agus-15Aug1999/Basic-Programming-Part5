import random

def prime_number(number, k=5):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
        
    s = 0
    d = number - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, number - 2)
        x = pow(a, d, number)
        if x == 1 or x == number - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
