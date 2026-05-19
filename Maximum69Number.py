# Maximum 69 Number :
# In this problem, we are given a positive integer num consisting of digits 6 and 9 only. We need to return the maximum number you can get by changing at most one digit (6 can be changed to 9, and 9 can be changed to 6).

# Simple Python solution:
num = input()
print(int(num.replace('6', '9', 1)))  # it is used to replace the first occurrence of the digit '6' with '9' in the string representation of the number. The replace() method takes three arguments: the substring to be replaced ('6'), the substring to replace it with ('9'), and the maximum number of occurrences to replace (1). This means that only the first '6' found in the string will be replaced with '9', and any subsequent '6's will remain unchanged. After performing the replacement, we convert the resulting string back to an integer using int() to get the final maximum number.