def fun():
    m=input("enter any statement\n")
    n=[]
    for i in m :
        n.append(i)
    n.sort()
    n=''.join(n)
    print(n)
fun()