
from a01_listfunction import find_max, find_min, sum_list, average_list, median_list

# Creating lists using list comprehensions
list1 = [i for i in range(1, 11)]  # A list of numbers from 1 to 10
list2 = [i**2 for i in range(1, 11)]  # A list of squares of numbers from 1 to 10
list3 = [i for i in range(10, 0, -1)]  # A list of numbers from 10 to 1 (descending)

# Demonstrating the functions
print("List 1:", list1)
print("Max:", find_max(list1))
print("Min:", find_min(list1))
print("Sum:", sum_list(list1))
print("Average:", average_list(list1))
print("Median:", median_list(list1))

print("\nList 2:", list2)
print("Max:", find_max(list2))
print("Min:", find_min(list2))
print("Sum:", sum_list(list2))
print("Average:", average_list(list2))
print("Median:", median_list(list2))

print("\nList 3:", list3)
print("Max:", find_max(list3))
print("Min:", find_min(list3))
print("Sum:", sum_list(list3))
print("Average:", average_list(list3))
print("Median:", median_list(list3))
