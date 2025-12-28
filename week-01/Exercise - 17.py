import random

numbers = []

for i in range(8):
    numbers.append(random.randint(1, 100))

print("Numbers:", numbers)

biggest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > biggest:
        biggest = num
    if num < smallest:
        smallest = num

print("Biggest number:", biggest)
print("Smallest number:", smallest)