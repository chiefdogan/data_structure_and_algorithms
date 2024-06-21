# 4-factorize.py
def factorize(number):
    factors = []
    divisor = 2
    while number >= divisor:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    print(factorize(100))  # Output: [2, 2, 5, 5]
    print(factorize(37))   # Output: [37]
