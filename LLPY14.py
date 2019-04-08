#14
a = [int(s) for s in input().split()]
summ = 0
i = 0
j = 1 
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            summ = summ + 1

print(summ)
        
