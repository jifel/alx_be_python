#using nested loops to print a square pattern 

pattern_size = int(input("Enter the size of the pattern: "))

row = 1
while row <= pattern_size:

    for i in range(1, pattern_size + 1):
        for j in range(1, pattern_size + 1):
            print("*", end="")
        print()  
        row += 1  
