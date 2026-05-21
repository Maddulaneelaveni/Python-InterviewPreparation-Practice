# Palindrome number :   (Leetcode - 9)
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
original_num=num  # it is used to store the original number before we start reversing it. 
reversed_num=0    # it is used to store the reversed version of the number as we build it up. We initialize it to 0 because we will be adding digits to it as we reverse the number.
while num>0:
    digit=num%10   # it is used to extract the last digit of the number. We do this by taking the modulus of the number by 10, which gives us the remainder when the number is divided by 10. For example, if num is 123, then digit will be 3.
    reversed_num=reversed_num*10+digit # it is used to build up the reversed number by adding the extracted digit to the end of the current reversed number. We multiply the current reversed number by 10 to shift its digits to the left, and then add the new digit to the end. For example, if reversed_num is currently 12 and digit is 3, then after this line, reversed_num will become 123.
    num=num//10    # it is used to remove the last digit from the number. We do this by performing integer division of the number by 10, which effectively shifts the digits to the right and discards the last digit. For example, if num is 123, then after this line, num will become 12.
if original_num==reversed_num:
    print("Palindrome") 
else:
    print("Not a palindrome")

# Time complexity: O(n) where n is the number of digits in the number. This is because we need to iterate through each digit of the number to reverse it.
# Space complexity: O(1) because we are using only a constant amount of extra space to store the reversed number and the original number.

