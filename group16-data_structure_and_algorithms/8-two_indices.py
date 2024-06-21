# 8-two_indices.py
def two_indices(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index

if __name__ == "__main__":
    print(two_indices([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(two_indices([3, 2, 4], 6))       # Output: [1, 2]
