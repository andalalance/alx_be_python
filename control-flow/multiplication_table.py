#Use a for loop to generate and print the multiplication table for a given number.

number = int(input("Enter a number to see its multiplication table: "))

counter = 1

for i in range(10):    
    print(f"{number} * {counter} = {counter * number}")
    counter += 1

