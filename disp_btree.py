# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:26:21 2022

@author: talukr

[ 9, 4, 8,2, 3, 1,7]

               9, 
        4,          8, 
    2,      3,  1,      7

[ 7, 4, 8,2, 3, 1,9]
               7, 
        4,          8, 
from collections import defaultdict
    2,      3,  1,      9

[ 8, 4, 7,2, 3, 1,9]
               8, 
        4,          7, 
    2,      3,  1,      9
    
n:7 tot_dep:3 a:[4, 3, 7, 2, 9, 1, 8]
           4
       3       7
     2   9   1   8
"""
from pprint import pprint
import math
from typing import List
from collections import defaultdict


def li(i:int)->int: # get left index pos of node at pos i 
    li = 2*i+1
    return 

def ri(i:int)->int: # get right index pos of node at pos i 
    ri = 2*i+2
    return

def pi(i:int)->int: # get parent index pos of node at pos i 
    pi = math.ceil(i/2)
    return


'''
si = math.floor(n//2)
ei = n
max_dp = lambda n:int(math.log2(n)) if n > 0 else 0

n dp si ei
1 0  0  1
2 1  1  2
3 1  1  3
4 2  3  4
5 2  3  5
6 2  3  6
7 2  3  7
8 3  7  8
9 3  7  9

si = 2**dp - 1
ei = min(2**(dp+1) - 1, n)
9 2  3  7
'''
def rangei(n:int, dp:int, lvl:int)->int: # get starting index of adj node
    # si = math.floor(n//2)
    # if si > n:
    # ei = n
    si = 2**dp - 1
    ei = min(2**(dp+1) - 1, n)
    return [si, ei]

# 0 1 3 7 15        
# gets lspaces needed at each lvl
def get_spaces_by_ht(h):
	if h == 0: return 0
	return 2*get_spaces_by_ht(h-1) +1



class Sort():
    def __init__(self):
        self.cnt = 0
    
    def tot_depth(self, n):
        res = int(math.floor(math.log2(n+1)))
        return res
    
    tot_height = lambda self, n:int(math.log2(n)) if n>0 else 0
    
    def node_height(self, a, i, n):
        if n == 0 or i>= n: return -1
        lh = self.node_height(a, 2*i+1, n)
        rh = self.node_height(a, 2*i+2, n)
        h = max(lh, rh) + 1
        return h

    def node_depth(self, i, n):
        dt = int(math.floor(math.log2(i+1)))
        return dt
    
    def max_nodes_same_dt(self, h:int)->int:
        """
        ht mnsh
        0  1
        1  2
        2  4
        """
        max_nodes_at_same_dp = 2**h
        # print(f"2**{h} = {max_nodes_at_same_dp}")
        return max_nodes_at_same_dp
    
    def default_to_regular(self, d):
        if isinstance(d, defaultdict):
            d = {k: self.default_to_regular(v) for k, v in d.items()}
        return d   

      
    def disp_tree(self, a):
      n = len(a)
      ht = self.tot_height(n)
      dp = self.tot_depth(n)
      i = 0
      ei = 0
      dd = defaultdict(list)
      dd_lspaces_by_ht = defaultdict(int)
      dd_sib_space_by_ht = defaultdict(int)
      dd_adj_space_by_ht = defaultdict(int)


      for h in range(10):
          tht = get_spaces_by_ht(h)
          dd_lspaces_by_ht[h] = get_spaces_by_ht(h)
          # print(f"my spaces({h}) => {tht}")
      # ppr int(dd_lspaces_by_ht)
      while i < n: 
          node_ht = self.node_height(a, i, n)
          dd[node_ht].append(a[i])
          # print(f"{a[i]}", end =",")
          # if i == ei:
          #     print("")
          [si, ei] = rangei(n, dp, i)
          i += 1
      pprint(dd)
      # print by height
      for ht in dd.keys():
          nodes_of_same_ht = dd[ht]
          lspace = dd_lspaces_by_ht[ht]
          sib_space = max(0, dd_lspaces_by_ht[ht+1])
          adj_space = max(0, dd_lspaces_by_ht[ht+1])
          print(f"h:{ht} lspace:{lspace} sib:{sib_space} adj:{adj_space} {dd[ht]}")

      ht_ll = list(dd.keys())
      # ht_ll.sort()
      print(ht_ll)
      for ht in ht_ll:
          nodes_of_same_ht = dd[ht]
          lspace = dd_lspaces_by_ht[ht]
          sib_space = max(0, dd_lspaces_by_ht[ht+1])
          adj_space = max(0, dd_lspaces_by_ht[ht+1])

          print(f"{'>'*lspace}", end="")
          is_sib = False
          len_nodes_same_ht = len(nodes_of_same_ht)
          for i,v in enumerate(nodes_of_same_ht):
              # print(f"{v:>1}", end="")
              print(f"{v*2:>2}", end="")

              if i < len_nodes_same_ht - 1:
                  print(f"{'-'*adj_space}", end="")
              is_sib = ~is_sib
          print()
# main
a = [4,3,7,2,9,1,8,0,1,2,3,4,5,6,7]
'''
n=15
start of height 
0:n//2=7, a[7] = 0 
    a[7:7*2+1] = [0, 1, 2, 3, 4, 5, 6, 7]
1:n//4=3  a[3] = 4
    a[4:4*2+1]
    
         4
    3         7
 2,   9,   1,   8,
0,1  2,3  4,5  6,7

'''
s = Sort()
print(f"s:{a}")
s.disp_tree(a)
