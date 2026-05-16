# AddDigits
# In this problem, we are given a non-negative integer num, and we need to repeatedly add all its digits until the result has only one digit. We need to return that single-digit result.

# Simple Python solution:
num = int(input())  
while num >= 10: # we use a while loop to check if the number has more than one digit (i.e., if it is greater than or equal to 10). If it does, we will continue to add its digits together until we get a single-digit result.
    num = sum(int(d) for d in str(num))     
print(num)



# DSA solution:
num = int(input())
if num == 0:
    print(0)
else:
    print(1 + (num - 1) % 9) # in simple, we are calculating the digital root of the number using the formula 1 + (num - 1) % 9. The digital root is the single-digit result obtained by repeatedly adding the digits of a number until only one digit remains. The formula works because the digital root of a number is equivalent to its value modulo 9, with a special case for numbers that are multiples of 9 (where the digital root is 9 instead of 0). By using this formula, we can directly compute the final single-digit result without needing to perform multiple iterations of adding digits together.
