# max sum of bin tree
class node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_sum(s:node, total:int=0, max:int=0)->int:
  if s is None:
    return total
  total += s.val
  # print(f"after adding {s.val} tot:{total}")
  lt = max_sum(s.left, total)
  rt = max_sum(s.right, total)
  # print(f"comparing {lt} to {rt}")
  if lt > rt:
    return lt
  return rt

# main
""""
               50
          +----+----+
         30         90 
       +--+--+     +-+-+
                  80
                +--
                70 
"""
if __name__ == "__main__":
  s = node(50)
  s.left = node(30)
  s.right = node(90)
  s.right.left = node(80)
  s.right.left.left = node(70)
  print(f"{max_sum(s)}")
