def oddfinder(n):
    counter = 0
    for i in range(2,n+1):
        if(n%i == 0):
            counter = counter +1
            

    if(counter > 1):
        return 0
    else:
        return n

low = int(input())
high = int(input())
lis1 = []
lis2 = []
count,liscount = 0,0

if(low>2):
    for i in range(2,high+1):
        x = oddfinder(i)
        y = oddfinder(i+6)

        lis1.insert(liscount,x)
        lis2.insert(liscount,y)

        liscount = liscount +1

for i in range(len(lis1)):
    check = lis1[i] +6
    for j in range(len(lis2)):
        if((check == lis2[j]) and (check < high)):
            count = count +1
            
print(count)
