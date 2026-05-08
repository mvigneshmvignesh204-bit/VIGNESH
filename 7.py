n = int(input("Enter a positive no: "))
total_sum = 0
if n <= 0:
    print("Please enter a positive integer.")
else:
    
    for number in range(1, n + 1):
        total_sum += number  
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")

