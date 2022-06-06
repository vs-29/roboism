def card():
    while True:
            ccnum=input("enter creditcard no of 16 digits\n")
            if (len(ccnum)==16):
                break
            else:
                print("invalid input\n")
    h="************"
    for i in range(0,4):
        h=h+str(ccnum[i+12])
    print(h)
card()