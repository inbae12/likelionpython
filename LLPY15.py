a = [str(s) for s in input().split()]

dic = {}

for i in a:
    if i not in dic:
         dic[i] = 0
    else:
         dic[i] += 1
    print(dic[i])
