# Plus One : 
# It is a problem where we are given a non-empty array of digits representing a non-negative integer, and we need to add one to the integer. 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. 
# We need to return the resulting array of digits after adding one to the integer.

# simple Python solution :
digits = list(map(int, input().split()))       # give simple input like this : 1 2 3
num = int("".join(map(str, digits)))          # it is used to convert the list of digits into a single integer. We first convert each digit in the list to a string using map(str, digits), and then we join these strings together using "".join() to form a single string that represents the entire number. Finally, we convert this string back to an integer using int(). For example, if digits is [1, 2, 3], then num will become 123.
num += 1                                     # it is used to add one to the integer that we just created from the list of digits. This is a simple arithmetic operation that increments the value of num by 1. For example, if num is currently 123, then after this line, num will become 124.
print(list(map(int, str(num))))        # it is used to convert the resulting integer back into a list of digits. We first convert the integer num back into a string using str(num), which allows us to access each digit as a character. Then, we use map(int, str(num)) to convert each character back into an integer, and finally, we wrap this in list() to create a list of digits. For example, if num is 124, then this line will output [1, 2, 4].

# Time complexity: 0(n)
# Space complexity: O(n)

