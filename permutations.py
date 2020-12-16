
def perms_recursive(a:list, lo, hi):
    # global cnt
    # import pdb;pdb.set_trace()
    if lo == hi:
        # cnt += 1
        print( "".join(a), " " , cnt)
    for i in range(lo, hi+1):
        # cnt+=1
        # print(f"swapping {i} with {lo} {hi}")
        a[i], a[lo] = a[lo], a[i]
        perms_recursive(a, lo+1, hi)
        a[i], a[lo] = a[lo], a[i]

def perm(s):
    a = list(s)
    # swap 1st char with all remaining elems in arr
    for i in range(0,len(a)):
        a[0], a[i] = a[i], a[0]
        # print("".join(a))
        #rotate
        for j in range(1, len(a)+1):
            # print(f"{a[0]}{(a[i:])}{a[1:i]}")
            sec_part = "".join(a[j:])
            tri_part = "".join(a[1:j])
            print(f"{a[0]}{sec_part}{tri_part}")
        

#main
if __name__ == "__main__":
    s = "abcd"
    perms_recursive(list(s), 0, len(s)-1)
    # perms((s))
