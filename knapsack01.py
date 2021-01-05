# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:45:58 2021
@author: talukr
Example of Dynamic Programming aka DP
Link: 3 01 Knapsack Recursive
https://www.youtube.com/watch?v=kvyShbFVaY8

Sample Output:
***> w:7 n:3
 > chose wt:1
 > picking 1
**> w:6 n:2
  > chose wt:5
  > picking 5
*> w:1 n:1
   > chose wt:10
   > !too much for wt:10 w:1
**> not picking 5 n:2
*> w:6 n:1
   > chose wt:10
   > !too much for wt:10 w:6
***> not picking 1 n:3
**> w:7 n:2
   > chose wt:5
   > picking 5
*> w:2 n:1
    > chose wt:10
    > !too much for wt:10 w:2
**> not picking 5 n:2
*> w:7 n:1
    > chose wt:10
    > !too much for wt:10 w:7
6
"""

nest = 0
is_new_at_this_level = True

def pprint(s, n):
    global nest
    global is_new_at_this_level
    if is_new_at_this_level:
        print("*"* n, end="> ")
        print(s)
        is_new_at_this_level = False
    else:
        print(" "* nest, end="> ")
        print(s)
    # print("")
    
def knapsack(wt, val, w, n)->int:
    global nest, is_new_at_this_level
    # print("*"* nest, end="> ")
    nest+=1
    is_new_at_this_level = True
    pprint(f"w:{w} n:{n}", n)
    pprint(f"chose wt:{wt[n-1]}", n)
    # import pdb;pdb.set_trace()
    if n == 0 or w == 0:
        pprint(f"!!not valid as n:{n} w:{w}", n)
        nest-=1
        is_new_at_this_level = True        
        return 0
    if wt[n-1] > w:
        pprint(f"!too much for wt:{wt[n-1]} w:{w}", n)
        nest-=1
        is_new_at_this_level = True        
        return 0
    elif wt[n-1] <= w:
        # pick or leave
        pprint(f"picking {wt[n-1]}", n)
        ch1 = wt[n-1] + knapsack(wt, val, w-wt[n-1], n-1)
        
        pprint(f"not picking {wt[n-1]} n:{n}", n)
        ch2 = knapsack(wt, val, w, n-1)
        return max(ch1, ch2)
      
#main
wt  = [10, 5, 1]
val = [20, 50, 100]
w = 7
res = knapsack(wt, val, w, len(wt))
print(res)
