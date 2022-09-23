#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:17:40 2022

@author: talukr
"""

# https://neetcode.io/courses/dsa-for-beginners/26
# https://neetcode.io/courses/dsa-for-beginners/27
# https://www.geeksforgeeks.org/top-20-hashing-technique-based-interview-questions/

from typing import List
import random
import sys

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return 'Pair(' + str(self.key) + ", " + str(self.val) + ')'


class HashMap:

    def __init__(self, sz = 2):
        self.size = 0
        self.capacity = sz
        self.map = [None] * self.capacity

    def _hash(self, key):
        index = hash(key) % self.capacity
        return index

    def stats(self):
        print(f"size/capacity ({self.size}/{self.capacity})")

    def put(self, k, v):
        index = self._hash(k)
        while True:
            if self.map[index] == None: # new insert
                self.map[index] = Pair(k, v)
                self.size += 1
                if self.size > self.capacity // 2:
                    print(f"time to rehash u/t:{self.size}/{self.capacity}")
                    self.rehash()
                return
            elif self.map[index].key == k: # overwrite val
                self.map[index].val = v
                return
            # cant find available slot, look for next slot
            index += 1
            index = index % self.capacity
        return


    def get(self, k)->str:

        index = self._hash(k)
        while self.map[index] != None:
            if self.map[index].key == k:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def pop(self, k)->str:
        pass

    def show(self):
        for i,v in enumerate(self.map):
            if v:
                print(f"index:{i} {v.key}:{v.val}")

    def rehash(self):
        self.capacity *= 2
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        oldMap = self.map
        self.map = newMap
        self.size = 0 # reset the size before copying old values
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)


    def keys(self)->List:
        pass

# main
menu = """
~~~~Menu~~~~
1. Show stats
2. Push a key
3. Get by key
4. Show all Values
5. Exit

fruits = [
 "apple",
 "banana",
 "chikoo",
 "date",
 "eggplant",
 "fig",
 "guava",
 "hazelnut",
 "icecream",
 "jelly",
 "kiwi",
 "lemon",
 "mango",
 "nutmeg",
 "orange",
 "pear",
 "quesadilla",
 "radish",
 "spinach",
 "tapioca",
 "upma",
 "vada",
 "watermelon",
 "xacuti",
 "yam",
 "zest",
]


h = HashMap(4)
h.stats()
h.put("a", "apple")
h.stats()
print(f"[ {h.get('a')} ]")
while True:
    #opt = int(input(f"{menu}"))
    print(f"{menu}", end="")
    opt_raw = (sys.stdin.readline())
    try:
        opt = int(opt_raw.strip())
    except ValueError as ve:
        print("ValueError seen with [{opt}]")
    print(f"you chose {opt}")
    if opt == 1:
        h.stats()
    elif opt == 2:
        f = random.choice(fruits)
        record = Pair(f[0], f)
        print(f"pushing {record}")
        h.put(f[0], f)
    elif opt == 3:
        k = input("Enter a key:")
        v = h.get(k)
        print(f"{k}:{v}")
    elif opt == 4:
        h.show()
    elif opt == 5:
        sys.exit(0)
    else:
        print(f"opt:[{opt}] unsure what to do..")

