#pizza generator
print("Welcome to pizza Shop ...")
size = input("what size of pizza do you want small,medium,large     ")
add_pepper = input("Do want add extra pepper")
cheese = input("Do you want cheese extra!!!!!!!")
bill = 0
if size == "large":
    bill+=20
elif size == "medium":
    bill+=15
else:
    bill+=25
#adding pepper
if add_pepper == "Y":
    bill+=5
else:
    bill+=3
#adding extra cheese
if cheese == "Y":
    bill+=10

print("Thank you choosing our pizza!!!")
print(f"Your total bill ${bill}")             

