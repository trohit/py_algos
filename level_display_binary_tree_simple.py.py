class node:
  def __init__(self, val:int, next=None):
    self.val = val
    self.left = None
    self.right = None

def height(s:node)->int:
  if s is None:
    return 0
  if s.left == None and s.right == None:
    return 1 
  lt = 1+height(s.left)
  rt = 1+height(s.right)
  if lt > rt:
    # print("ht:" + str(s.val) + "->lt " + str(lt))
    return lt
  # print(f"ht:" + str(s.val) + "->rt " + str(rt))
  return rt 

def level_disp(s:node, lvl = 0):
  if s is None:
    return
  h = height(s)
  for i in range(h, 0, -1):
    print(f"nodes at height {i}:")
    ldfs(s, i)
  
def ldfs(s:node, h:int=0):
  if s == None:
    return 
  ldfs(s.left, h)
  if height(s) == h:
    print(f">> at ht:{h} : {s.val}")
  ldfs(s.right, h)


#main
""""
               50
          +----+----+
         30         90 
       +--+--+     +-+-+
                  80
                +--
                70 
"""
s = node(50)
s.right = node(90)
s.left = node(30)
s.right.left = node(80)
s.right.left.left = node(70)
level_disp(s)
