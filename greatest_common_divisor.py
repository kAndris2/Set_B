num1 = int(input("Enter a number.\n"))
num2 = int(input("Enter another number.\n"))

if num1 > num2:
    max = num1
elif num2 > num1:
    max = num2

gcd = 0

for i in range(1, max+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("The greatest common divisor of " + str(num1) + " and " + str(num2) + " is " + str(gcd))