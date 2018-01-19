def guess_fruit(basket):
    counter = 0
    while counter < 5:
        user_choce = input("Enter you choie of fruit ")
        if user_choce.strip().upper() in basket:
            print("Your guess is right")
        else:
            counter = counter + 1
            print(counter)
            if counter == 5:
                print("you ran out of options")


def main():
    fruits = ["APPLE","ORANGE","MANGO","KIWI","BLUEBERRY"]
    guess_fruit(fruits)

main()