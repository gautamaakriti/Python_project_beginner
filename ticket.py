print("Welcome to the wild rollercoster ride fun with Aakrit")
height = int(input("What is your heingt in cm? "))
bill = 0
# now add the loop if 

if height >= 120:
    print("You can ride the rollwer coster ")
    age = int(input("What is your age: "))
    if age < 12:
        bill = 5
        print("Please pay $5 as child ticket.")
    elif age <= 18 :
        bill = 7
        print("Please pay $7 as youth ticket.")
    elif age >=45 and age <= 55:
        print("Bill is on the house.")
    else:
        bill = 12
        print("Please pay $12 as adult ticket.")
    
    wants_photo = input("Do you wanna take photo if yess, write 'Y' if not write 'N', Note that the photo will be charged.. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total final bill is {bill}.")
else:
    print("Sorry shorty you need to grow up...")
