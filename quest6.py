def fun() :
    prime=[]
    try:
        a=list(map(int,input("Enter the range into which prime numbers are to found keeping a blank space\n").split()))
        if len(a)!=2: # 1 5 2 2 7 1
            s
    except:
        print("re-enter the correct input")
        fun()
    for i in range(a[0],a[1]): 
        c = True
        for j in range(2,int(i/2)):
            if i%j==0:
                c=False
                break
        if c==True:
            prime.append(i)
    print(f"In the range of {a[0]} and {a[1]} prime numbers are {prime}")
fun()
