# AddDigits
# In this problem, we are given a non-negative integer num, and we need to repeatedly add all its digits until the result has only one digit. We need to return that single-digit result.

# Simple Python solution:
num = int(input())  
while num >= 10: # we use a while loop to check if the number has more than one digit (i.e., if it is greater than or equal to 10). If it does, we will continue to add its digits together until we get a single-digit result.
    num = sum(int(d) for d in str(num))     #
print(num)