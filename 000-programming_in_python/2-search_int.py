# 2-search_int.py
def find_first_occurrence(my_list, num):
    for index, value in enumerate(my_list):
        if value == num:
            return index
    return -1  # Return -1 if the number is not found

if __name__ == "__main__":
    print(find_first_occurrence([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5))  # Output: 4
    print(find_first_occurrence([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 7))  # Output: -1
