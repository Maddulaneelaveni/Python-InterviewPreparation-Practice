# Subtract Product and Sum :
# In this problem, we are given a positive integer n, and we need to find the difference between the product of its digits and the sum of its digits.

# Simple Python solution:
num = int(input())
digits = [int(d) for d in str(num)] # it is used to extract the digits of the input number and store them in a list. We first convert the number to a string using str(num), which allows us to access each digit as a character. Then, we use a list comprehension [int(d) for d in str(num)] to iterate through each character (digit) in the string, convert it back to an integer using int(d), and create a list of these integer digits. For example, if num is 123, then digits will become [1, 2, 3].
product = 1
for d in digits:
    product *= d  # it is used to calculate the product of the digits in the list. We initialize a variable product to 1, and then we iterate through each digit d in the list of digits. For each digit, we multiply the current value of product by that digit (product *= d), which effectively accumulates the product of all the digits. For example, if digits is [1, 2, 3], then after this loop, product will become 1 * 2 * 3 = 6.
print(product - sum(digits))

# TC: O(n) where n is the number of digits in the input number. This is because we need to iterate through the digits to calculate both the product and the sum.
# SC: O(n) because we are storing the digits in a list, which takes up space proportional to the number of digits in the input number.



# DSA solution:
num = int(input())
product = 1
total = 0
while num > 0:
    digit = num % 10      # it is used to extract the last digit of the number. We do this by taking the modulus of the number by 10, which gives us the remainder when the number is divided by 10. For example, if num is 123, then digit will be 3.
    product *= digit     # it is used to calculate the product of the digits as we extract them. We initialize a variable product to 1, and then for each extracted digit, we multiply the current value of product by that digit (product *= digit), which effectively accumulates the product of all the digits. For example, if num is 123, then after processing the first digit (3), product will become 1 * 3 = 3. After processing the second digit (2), product will become 3 * 2 = 6. After processing the third digit (1), product will become 6 * 1 = 6.
    total += digit
    num //= 10
print(product - total)

# TC: O(log n) # where n is the input number. This is because the number of digits in a number is proportional to the logarithm of the number (base 10). Therefore, as we extract each digit, we are effectively iterating through the digits of the number, which takes O(log n) time.
# SC: O(1) because we are using only a constant amount of extra space to store the product, total, and the current digit. We are not using any additional data structures that grow with the size of the input number.