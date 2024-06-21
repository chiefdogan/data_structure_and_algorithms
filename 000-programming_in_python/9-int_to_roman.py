# 9-int_to_roman.py
def int_to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_numeral = ""
    for i in range(len(val)):
        count = n // val[i]
        roman_numeral += syms[i] * count
        n -= val[i] * count
    return roman_numeral

if __name__ == "__main__":
    print(int_to_roman(27))  # Output: XXVII
    print(int_to_roman(1994))  # Output: MCMXCIV
