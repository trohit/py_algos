# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:47:06 2022

@author: talukr

======================================
how_many_bytes    pow_10 pow_2 storage
======================================     
one               10^0   2^0    byte        
ten               10^1   2^4    bytes       
thousand          10^2   2^7    KB          
hundred thousand  10^4   2^14   100KB       
million           10^6   2^20   MB          
billion           10^9   2^30   GB          
trillion          10^12  2^40   TB          
quadrillion       10^15  2^50   PB          
quintillion       10^18  2^60   EB          

"""
import math
def powersOf2(n):
    if n == 0: return 1
    return 2 * powersOf2(n - 1)

def bitsNeeded(n):
    res = math.ceil(math.log2(n))
    return res

# main
powers_of_2_dd = {
    "one":{"num":0, "storage_bytes":"byte"},
    "ten":{"num":1, "storage_bytes":"bytes"},
    "thousand":{"num":2, "storage_bytes":"KB"},
    "hundred thousand":{"num":4, "storage_bytes":"100KB"},
    "million":{"num":6, "storage_bytes":"MB"},
    "billion":{"num":9, "storage_bytes":"GB"},
    "trillion":{"num":12, "storage_bytes":"TB"},
    "quadrillion":{"num":15, "storage_bytes":"PB"},
    "quintillion":{"num":18, "storage_bytes":"EB"},

}

print(f"{'how_many_bytes':<17} {'pow_10':^6} {'pow_2':^4} {'storage':<12}")
for i in powers_of_2_dd:
    record = powers_of_2_dd[i]
    ten_pow= int(record["num"])
    binary_power = bitsNeeded(10**ten_pow)
    storage_bytes = record["storage_bytes"]
    print(f"{i:<17} 10^{ten_pow:<3} 2^{binary_power:<4} {storage_bytes:<12}")

