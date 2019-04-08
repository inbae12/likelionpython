#9
a = str(input(""))
b = a.find('h')
c = a.rfind('h')

z = a[:b]
z2 = a[c+1:]
print(z,z2,sep='')
