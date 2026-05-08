user_input = input("Enter a number: ")


if user_input.isdigit():
    number = int(user_input)
   
    if number >= 0:
        while number >= 0:
            print(number)
            number = number - 1
    else:
        print("Please enter a non-negative number.")
else:
    print("Invalid input. Please enter an integer.")

