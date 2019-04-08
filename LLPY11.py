a = int(input())
b,c,n = 1, 1, 2

while n < 10:
  b, c = c, c + b
  n += 1
  if n == a:
      print(c)
      break
if n != a:
  print("-1")
