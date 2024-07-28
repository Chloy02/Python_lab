for i in range(1,6):
    print("*"*i)
    
print("====================")

for i in range(1, 6):
        # Print leading spaces for the pyramid structure
        for j in range(5 - i):
            print(" ", end="")
        
        # Print letters
        for j in range(i):
            print(chr(65 + j), end="")
        
        print()  # Move to the next line