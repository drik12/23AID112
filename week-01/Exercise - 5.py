str1 = input("Enter a Number: ")
str2 = input("Enter another Number: ")

num1 = int(str1)
num2 = int(str2)

sum = num1 + num2
difference = num1 - num2
product = num1 * num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)

if num1 > num2:
    print("Bigger Number:", num1)
elif num2 > num1:
    print("Bigger Number:", num2)
else:
    print("Both numbers are equal")