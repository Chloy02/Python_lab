months = [
    ("January", 31),
    ("February", 28),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

print("This program will give you the number of days in a month")

chosen_month = str( input("Enter the month name: "))
year = int(input("Enter the year: "))

month_exist = False

for i in range(0, 12):
    if chosen_month.lower() == months[i][0].lower():
        month_exist = True
        if year % 4 == 0 and chosen_month.lower() == months[1][0].lower():
            print("The number of days in ", months[i][0], " is: 29")
        else:
            print("The number of days in ", months[i][0], " is: ", months[i][1])
        break
    if not month_exist:
        print("Enter valid month")
        continue
