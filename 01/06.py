number = int(input("Enter a four digit number: "))

sum_dig = 0 
rev_num = 0 
while number > 0 :
    digit = number % 10
    sum_dig += digit
    rev_num = rev_num*10 + digit
    number = int(number/10)
    
print("Sum of the digits of the entered number is: ", sum_dig)

print("The reversed number is: ",rev_num)