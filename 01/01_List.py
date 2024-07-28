l1 = [1,2,3,4,5,6,17,8,9]
# Declaring list and using inbuilt function sum to find sum
print("The sum of items in the list l1 is: ", sum(l1))

product = 1
# Initialising product and defining for loop to get product of list items
for i in range(0,len(l1)-1):
    product *= l1[i]
    
print("The product of the items in the list is: ",product)

# Finding largest number from list 
largest_num = 0 

for i in l1:
    if i > largest_num:
        largest_num = i 

print("The largest number in the list is: ",largest_num)

# Or using inbuilt function 

print("The largest number in the list using built in function is: ",max(l1))

# FInidng smallest number from list 

print("The smallest number from the given list is:", min(l1))
