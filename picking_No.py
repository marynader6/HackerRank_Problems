def pickingNumbers(a):
    count=0
    myMax = 0
    a.sort(reverse=True)
    for i in range(len(a)):
        for j in range(i,len(a)):
            if((abs(a[i] - a[j] ) == 1) or (a[i] == a[j])):
                count += 1
            else:
                break
        if(count > myMax):
            myMax = count
        count = 0
    return myMax

a = [1,2,2,1,3,2]

print(pickingNumbers(a))