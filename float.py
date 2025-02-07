def user_numbers():

    number_range1 = float(input("Write a number to begin your range: "))
    number_range2 = float(input("Write a number to end your range: "))
    number_user = float(input("Write a number to see if it's in range: "))
    i = 0

    while (i == i):
        if (number_user >= number_range1 and number_user <= number_range2):
            print("Your number is in range!")
        else:
            print("Your number is not in range.")

        number_user = float(input("Write a number to see if it's in range: "))
        i = i + 1

    return number_user

user_numbers()