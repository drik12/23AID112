age = input("Enter your age: ")
age_num = int(age)
if age_num < 13:
    print("You are a child.")
elif 13 <= age_num <= 17:
    print("You are a teenager.")
elif 18 <= age_num <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")