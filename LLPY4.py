#4
a = int(input("숫자 a를 입력해주세요"))
b = int(input("숫자 b를 입력해주세요"))

x = b/a

if b == 0:
    print("many solutions")
elif x % 1 != 0:
    print("NO SOLUTION")
elif x % 1 == 0:
    print(int(x))

