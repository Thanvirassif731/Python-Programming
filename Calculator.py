print("This is an Calculating program! Please follow the instructions given below!!")
a = int(input("Enter a number to Calculate : "))
b = int(input("Enter another number to Calculate : "))
c = input("Type the given character that you should able to calculate [+,-,*,/,%] : ")

if c=='+':
  print(a+b)
elif c=='-':
  print(a-b)
elif c=='*':
  print(a*b)
elif c=='/':
  print(a/b)
elif c=='%':
  print(a%b)
else:
  print("Sorry!!! The give Character is not matched! Please try again!")
