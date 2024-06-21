# 5-sum_even.py
def sum_even_numbers(my_list):
    return sum(num for num in my_list if num % 2 == 0)

if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12
