A = 1
while A <= 5:
    B =6-A
    while B>1:
        if B!=1:
            print(A,B, end=', ')
        elif A!=5:
            print(A,B,end=' ** ')
        else:
            print(A,B)
        B=B-1
    A=A+1
