import random

def reverse_string(s: str):
    result = ""
    index = len(s) - 1
    while index >= 0:
        result += s[index]
        index -= 1
    return result
print(reverse_string("Hello"))

def count_vowel(c: str):
    vowels = "AEIOU"
    count = 0
    for char in c.upper():
        if char in vowels:
            count += 1
    return count
print(count_vowel("hEllo wOrld"))


def sol23(s: str):
    words = []
    word = ""
    space = ' '
    last_index = len(s) - 1
    curr_index = 0
    # if s[len-1] != space:
    #     s = s + space
    for char in s:
        if char != space:
            word = word + char
        elif curr_index == last_index:
            words.append(word)
        else:
            words.append(word)
            word = ""
        curr_index += 1

    return words

print(sol23("Hello World"))


def is_palindrome(s: str):
    return s == reverse_string(s)

print(is_palindrome("madam"))

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
rect = Rectangle(5, 10)
print(rect)
print(f"Area: {rect.area()}")

def sol26(arr: list):
    return [x for x in arr if x % 2 == 0]
print(sol26([1, 2, 3, 4, 5, 6]))

# string = input("Enter a string: ")
# if string.isdigit():
#     print("The string is a number.")
# if string.isalpha():
#     print("The string is alphabetic.")

arr = [1, 2, 3, 4, 5, 6,7,8,9,10]
arr2 = [x if x % 3 == 0 else "_" for x in arr]
print(arr2)

import school as sch

sch.my_school.display_students()