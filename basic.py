a = int(input("Please enter a Year to find leap year : "))
if a/400==0:
    if a/100==0:
        print(f"{a} is a Leap Year!")
    else:
        print(f"{a} is not a Leap Year!!")
else:
    if a/4==0:
        print(f"{a} is a Leap Year!!!")
    else:
        print(f"{a} is not a Leap Year!!!!")