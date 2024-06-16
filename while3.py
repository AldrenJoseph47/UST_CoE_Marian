num = 1
# this line is commented

while num < 31:
    if num % 10 == 0:
        print(num)
        num += 1
    elif num % 10 != 0:
        print(num, end='-')
        num += 1
    else:
        print(num, end='-')
        num += 1