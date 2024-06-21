# 1-smallest_int.py
def get_smallest_integer(my_list):
    if not my_list:  # Check if the list is empty
        return None
    smallest = my_list[0]
    for num in my_list:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == "__main__":
    print(get_smallest_integer([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 1
