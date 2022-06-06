def fun():
    try:
        l=list(map(int,input("Enter the integer elements keeping blank space between them\n").split()))
    except:
        print("re-enter a correct input")
        fun()
    l.sort()
    c=0
    k=0
    while((k+c)<(len(l)-1)):

        if l[k+c]==l[k+c+1]:
            print(str(l[k+c])+" is repeated\n")
            k=k+1
        else :
            pass
        c=c+1
fun()