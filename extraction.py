l=['ICSE','CBSE']
i,c1,c2,b,s,e='Indian','Certificate','Central','Board','Scecondary','Education'
for f1 in l:
    for f2 in f1:
        if(f2=='I'):
            print(f2,'-',i)
            temp=f2
        elif (f2=='c'):
            if (temp=="I"):
                print(f2,'-',c1)
                temp=''
            else:
                print(f2,'-',c2)
        elif (f2=='B'):
            print(f2,'-',b)
        elif(f2=='S'):
            print(f2,'-',s)
        else:
            print(f2, '-',e)
    print("=======")