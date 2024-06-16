for i in range(1, 21):
    if (i==20):
        print(i, end=(''))
    elif i % 3 != 0:
        print(i, end=" - ")
    else:
        print(end="")