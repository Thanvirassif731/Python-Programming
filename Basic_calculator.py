first_number = int(input("Enter the 1st number here : "))
second_number = int(input("Enter the 2nd number here : "))
operator = input("Select an operator here ::: + - * / % :::")

if operator=='+':
    print(first_number+second_number)

elif operator == '-':
    print(first_number - second_number)

elif operator=='*':
    print(first_number*second_number)

elif operator=='/':
    print(first_number/second_number)

elif operator == '%':
    print(first_number % second_number)

else:
    print("Invalid Operator!!!")