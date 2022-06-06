def fun():
    a=list(map(int,input("Enter any integer value keeping blank space\n").split()))

    print (f"prior to swap: a= {a[0]} b ={a[1]}")
    a[0] = a[0] ^ a[1]
    a[1] = a[0] ^ a[1]
    a[0] = a[0] ^ a[1]
    print (f"After swap: a= {a[0]} b ={a[1]}")
fun()