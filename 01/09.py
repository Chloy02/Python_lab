lis = []

print("Enter the elements you want inside the tuple: ")

stop = True
# Using while loop to input elements in the list to be turned tuple 
while stop == True:
    user_input = input("Enter the element (or 'stop' to finish): ")
    if user_input.lower() == "stop":
        stop = False
    else :
        lis.append(user_input)
        
input_tup = tuple(lis)
# Made the list into tuple

list_of_rear_elements = []
# Getting the rear elements
for i in range(0,len(input_tup)):
    item = input_tup[i]
    list_of_rear_elements.append(item[-1])

# Printing the rear elements list 
print(list_of_rear_elements)