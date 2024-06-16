for num in range(1, 40,1):
    if num % 10 == 0:
        print(num,'-')
        num += 1
    elif num % 4 != 0:
        print(num,end='-')



