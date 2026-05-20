# Maximum 69 Number :   ( Leetcode - 1323 )
# In this problem, we are given a positive integer num consisting of digits 6 and 9 only. We need to return the maximum number you can get by changing at most one digit (6 can be changed to 9, and 9 can be changed to 6).

# Simple Python solution:
num = input()
print(int(num.replace('6', '9', 1)))  # it is used to replace the first occurrence of the digit '6' with '9' in the string representation of the number. The replace() method takes three arguments: the substring to be replaced ('6'), the substring to replace it with ('9'), and the maximum number of occurrences to replace (1). This means that only the first '6' found in the string will be replaced with '9', and any subsequent '6's will remain unchanged. After performing the replacement, we convert the resulting string back to an integer using int() to get the final maximum number.

# TC: O(n) where n is the number of digits in the input number. This is because the replace() method needs to scan through the string to find the first occurrence of '6' and perform the replacement.
# SC: O(n) because we are creating a new string as a result of the replace operation, which takes up space proportional to the number of digits in the input number.



# DSA solution:
num = list(input())
for i in range(len(num)):
    if num[i] == '6':
        num[i] = '9'
        break
print(int("".join(num)))

# TC: O(n) where n is the number of digits in the input number. This is because we need to iterate through the list of digits to find the first occurrence of '6' and perform the replacement.
# SC: O(n) because we are creating a list of characters from the input string, which takes up space proportional to the number of digits in the input number. Additionally, we are creating a new string when we join the list back together, which also takes up space proportional to the number of digits.