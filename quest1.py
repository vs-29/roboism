def func():
    while True:

        try:
            list1=list(map(int,input("enter the elements with keeping blank space\n").split()))
            break
        except:
            print("invalid input\n")

    def reorder():
        comnd=(input("Enter a operation : 'asc','desc' or 'none'\n"))
        if comnd=="asc":
            list1.sort()
        elif comnd=="desc" :
            list1.sort(reverse=True)
        elif comnd=="none":
            pass
        else :
            print("Enter a valid operation")
            reorder()
    reorder()
    print("The reordered list is:"+str(list1))
func()