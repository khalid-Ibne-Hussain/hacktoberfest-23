def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
number = 17  # You can change this number to check other values
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
