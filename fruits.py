fruits = ["APPLE","ORANGE","MANGO","KIWI","BLUEBERRY"]
user_choce = input("Enter you choice of fruit")

if user_choce.strip().upper() in fruits:
    print("Your guess is right")
else:
    print("You missed")