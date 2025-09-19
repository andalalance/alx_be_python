#Utilize while loops and nested for loops to draw a simple text-based pattern.

outer_count = int(input("Enter the size of the pattern: "))
inner_count = outer_count
timer = outer_count

while outer_count > 0:
    while inner_count > 0:
        print("*", end="")
        inner_count -= 1 

    print()  # Move to a new line after each outer loop iteration    
    inner_count = timer
    outer_count -= 1
