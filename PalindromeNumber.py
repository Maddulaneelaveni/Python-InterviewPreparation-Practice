# Palindrome number
# It is a number that reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

# Simple Python solution :
num=int(input("Enter a number: "))
if str(num)==str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Time complexity: O(n) where n is the number of digits in the number. This is because we need to convert the number to a string and reverse it, which takes O(n) time.
# Space complexity: O(n) because we are creating a new string to store the reversed version of the number

# DSA solution (without string):

num=int(input("Enter a number: "))
original_num=num
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
if original_num==reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")