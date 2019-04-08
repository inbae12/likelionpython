#12
a = int(input())
b,c,n = 1, 1, 2

while n < 10:
  b, c = c, c + b
  n += 1
  if c == a:
    print(n)
    break
if c != a:
  print("-1")
