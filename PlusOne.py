# Plus One :  (Leetcode - 66)
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


# DSA Solution:
digits = list(map(int, input().split()))      # give simple input like this : 1 2 3
for i in range(len(digits)-1, -1, -1):        # in simple, we are iterating through the list of digits in reverse order, starting from the last index (len(digits)-1) and ending at the first index (0). The step -1 indicates that we are moving backwards through the list. This allows us to process the digits from right to left, which is necessary when adding one to the number represented by the list of digits.
    if digits[i] < 9:                     # it is used to check if the current digit is less than 9. If it is, then we can simply increment that digit by 1 and break out of the loop, because we don't need to worry about any carry-over to the next digit. For example, if the current digit is 3, then after this line, it will become 4, and we can stop processing further digits. 
        digits[i] += 1
        print(digits)
        break
    digits[i] = 0
else:
    digits.insert(0, 1)      # it is used to handle the case where all the digits in the list are 9. In this case, when we add one to the number, it will result in a new digit being added at the beginning of the list (the most significant digit). For example, if the input is [9, 9, 9], then after adding one, it will become [1, 0, 0, 0]. To achieve this, we insert a 1 at the beginning of the list using digits.insert(0, 1), and then we set all the existing digits to 0. This is done in the else block because it only executes if we have iterated through all the digits without finding any digit less than 9.
    print(digits)

# We can also do this in another way by using two pointers, one at the start and one at the end of the list, and we can move the pointers towards each other until we find a digit that is less than 9. Then we can increment that digit and set all the digits to the right of it to 0. If we reach the end of the list without finding a digit less than 9, then we can insert a 1 at the beginning of the list and set all the digits to 0.
# TWO POINTERS APPROACH:

digits = list(map(int, input().split()))
left, right = 0, len(digits) - 1 # we initialize two pointers, left and right, to the start and end of the list of digits, respectively. The left pointer starts at index 0 (the most significant digit), and the right pointer starts at index len(digits) - 1 (the least significant digit). We will use these pointers to traverse the list from both ends towards the center, allowing us to efficiently find the rightmost digit that is less than 9 and handle the carry-over when adding one to the number.
while right >= 0:     # we use a while loop to iterate through the list of digits from the rightmost end towards the left. The loop continues as long as the right pointer is greater than or equal to 0, which means we are still within the bounds of the list. This allows us to check each digit starting from the least significant digit and moving towards the most significant digit until we find a digit that is less than 9 or we exhaust all digits.
    if digits[right] < 9:
        digits[right] += 1 # it is used to increment the current digit by 1. This is done when we find a digit that is less than 9, which means we can simply add one to that digit without worrying about any carry-over to the next digit. For example, if the current digit is 3, then after this line, it will become 4.
        print(digits)
        break
    digits[right] = 0  # it is used to set the current digit to 0. This is done when we encounter a digit that is equal to 9, which means that adding one to it will result in a carry-over to the next digit. For example, if the current digit is 9, then after this line, it will become 0, and we need to continue checking the next digit to the left for further carry-over.
    right -= 1      # it is used to move the right pointer one step to the left. This allows us to check the next digit in the list for potential carry-over when we encounter a digit that is equal to 9. For example, if the current digit is 9 and we set it to 0, we need to move the right pointer to the next digit on the left to check if it is also 9 and requires further carry-over.
else:
    digits.insert(0, 1)
    print(digits)
