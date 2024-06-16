def find_max(numbers):
    max=list[0]
    for num in numbers:
        if num > max:
            max = num
    return max
list=[]
a=int(input('How many numbers ? '))
for i in range(a):
    b=int(input('enter the '+str(i+1)+' value : '))
    list.append(b)
max = find_max(list)
print("The largest number is:", max)