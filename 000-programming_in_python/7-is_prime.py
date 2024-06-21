# 7-is_prime.py
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print(is_prime(29))  # Output: True
    print(is_prime(15))  # Output: False
