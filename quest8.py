def fun():
    s=input("Enter any statement\n")
    num=0
    for i in s:
        try:
            num=num+int(i)
        except:
            pass
    print(num)
fun()