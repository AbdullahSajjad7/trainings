import math

def is_prime(n):
    if n > 1:   
        if n == 2:
            return True
        ceil_sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, ceil_sqrt_n + 1):
            if n % i == 0:
                return False
        return True
    else:
        print("Invalid Input")
        return False

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(10))
print(is_prime(13))
print(is_prime(23))
print(is_prime(27))
print(is_prime(29))
print(is_prime(31))
print(is_prime(32))

