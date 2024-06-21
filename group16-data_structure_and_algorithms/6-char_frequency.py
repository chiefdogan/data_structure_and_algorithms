# 6-char_frequency.py
def character_frequency(string):
    frequency = {}
    for char in string.lower():
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

if __name__ == "__main__":
    print(character_frequency("Hello, World!"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
