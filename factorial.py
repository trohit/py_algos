def fact(n:int=0)->int:
  if n <= 0:
    return (1)
  if n == 1:
    return (1)
  return fact(n-1) + fact(n-2)

#main
for i in range(0,10):
  print(f"{fact(i)}", end =" ")
