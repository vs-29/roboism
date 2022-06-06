def calc():
    a=int(input("Enter num1:"))
    b=input("enter a operation:")
    c=int(input("enter num2:"))
    if b=='.':
        print(a*c)
    elif b=='/':
        print(a/c)
    elif b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    else:
        print("invalid input..try again\n")
        calc()
while True:
    try:
        calc()
        break
    except:print ("enter valid inputs\n")
