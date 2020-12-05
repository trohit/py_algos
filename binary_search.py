l =[0,10,20,30,40,50,60,70,80,90,100]
def BinarySearch(a:list,n:int)->int:
  ctr = 1
  start = 0
  midpos = 0
  end = len(a)-1
  while end >= start :
    midpos=(end + start)//2
    print(f"c:{ctr} st:{start} m:{midpos} end:{end} m:{a[midpos]}")
    if ctr >10:
      return -1
    ctr+=1
    if a[midpos] == n:
      return midpos 
    if n > a[midpos]:
      print(">")
      start = midpos+1
    else:
      print("<")
      end = midpos-1

#main
for i in range(0,len(l)-1):
  print(f"searching for :{l[i]}")
  print (f"{BinarySearch(l,l[i] )}")
  
