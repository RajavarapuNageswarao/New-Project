# # #pizza generator
# # print("Welcome to pizza Shop ...")
# # size = input("what size of pizza do you want small,medium,large     ")
# # add_pepper = input("Do want add extra pepper")
# # cheese = input("Do you want cheese extra!!!!!!!")
# # bill = 0
# # if size == "large":
# #     bill+=20
# # elif size == "medium":
# #     bill+=15
# # else:
# #     bill+=25
# # #adding pepper
# # if add_pepper == "Y":
# #     bill+=5
# # else:
# #     bill+=3
# # #adding extra cheese
# # if cheese == "Y":
# #     bill+=10

# # print("Thank you choosing our pizza!!!")
# # print(f"Your total bill ${bill}")             

# print("The love calculator is calculating your score!!!!!!!!!!")
# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")

# # Remove spaces, numbers, and special characters from the names
# cleaned_name1 = "".join(e for e in name1 if e.isalpha())
# cleaned_name2 = "".join(e for e in name2 if e.isalpha())

# combined_names = cleaned_name1 + cleaned_name2
# lower_names = cleaned_name1 + cleaned_name2.lower()

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")

# first_digit = t + r + u + e
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")

# second_digit = l + o + v + e
# score = int(str(first_digit)) + str(second_digit)

# if (score < 10) and (score > 90):
#     print(f"your score is {score} you go together with mentor")
# elif(score >=40) and (score <= 50):
#     print(f"your score is {score} your like together")
# else:
#     print(f"your score is {score}")

#random numbers
# import random

# # first_random = random.randint(1,10)
# # second_random = random.random()
# # #third_random = random.uniform
# # print(f"first random number is {first_random}")
# # print(f"second random numbers is {second_random}")
# # #print(f"third random numbers is {third_random}")

# #heads and tails
# input("Enter the number    ")
# random_number = random.randint(0,1)
# if random_number == 1:
#   print("heads")
# else:
#   print("tails")  

#banker roulete
import random

# Define the names_string variable
names_string = "John, Alice, Bob, Sarah, Emma"

# Split the names_string into individual names
names = names_string.split(", ")

# Calculate the number of items in the list of names
num_items = len(names)

# Generate a random index to select a person
random_choice = random.randint(0, num_items - 1)

# Retrieve the person who will pay based on the random index
person_who_will_pay = names[random_choice]

# Print the selected person
print(person_who_will_pay + " will pay for the meal today.")
