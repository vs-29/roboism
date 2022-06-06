def fun():
    try:
        l=list(map(int,input("Enter any integer value keeping blank space\n").split()))
    except:
        print("re-enter a valid input")
        fun()
    freq={}
    for i in l :
        if i in freq :
            freq[i]=freq[i]+1
        else:
            freq[i]=0
    print(max(freq,key=freq.get))
fun()