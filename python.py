# #pizza generator
# print("Welcome to pizza Shop ...")
# size = input("what size of pizza do you want small,medium,large     ")
# add_pepper = input("Do want add extra pepper")
# cheese = input("Do you want cheese extra!!!!!!!")
# bill = 0
# if size == "large":
#     bill+=20
# elif size == "medium":
#     bill+=15
# else:
#     bill+=25
# #adding pepper
# if add_pepper == "Y":
#     bill+=5
# else:
#     bill+=3
# #adding extra cheese
# if cheese == "Y":
#     bill+=10

# print("Thank you choosing our pizza!!!")
# print(f"Your total bill ${bill}")             

print("The love calculator is calculating your score!!!!!!!!!!")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Remove spaces, numbers, and special characters from the names
cleaned_name1 = "".join(e for e in name1 if e.isalpha())
cleaned_name2 = "".join(e for e in name2 if e.isalpha())

combined_names = cleaned_name1 + cleaned_name2
lower_names = cleaned_name1 + cleaned_name2.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e
score = int(str(first_digit)) + str(second_digit)

if (score < 10) and (score > 90):
    print(f"your score is {score} you go together with mentos")
elif(score >=40) and (score <= 50):
    print(f"your score is {score} your like together")
else:
    print(f"your score is {score}")