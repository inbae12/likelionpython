#10
b=0
c=0
li = []
a = str(input("단어를 입력"))
if 'f' not in a:
    print("-1")
else:
    b = a.find('f')
    c = a.rfind('f')
    if b==c:
        print(b)
    else:
        print(b,c)

        


    
