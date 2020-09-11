#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
            numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                        'X': 10, 'V': 5, 'I': 1}
            total = 0
            for char in roman_string[::-1]:
                if numerals[char] > total or char == last:
                    total += numerals[char]
                else:
                    total -= numerals[char]
                last = char
            return total
