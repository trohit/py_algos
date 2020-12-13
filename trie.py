"""trie module doc - https://en.wikipedia.org/wiki/Trie"""
class node:
  """this is a trie node"""
  def __init__(self)->None:
    self.cnt = 0
    self.val = None
    self.child = {}
    self.is_end_of_word = False

def add(s:node, uid:str)->None:
  t = s
  for i in range(len(uid)):
    char = uid[i]
    if char not in t.child.keys():
      # new node in trie
      t.child[char] = node()
      t.child[char].cnt = 1
      t.child[char].val = char
    else:
      # if node already exists, increment the ref count  
      t.child[char].cnt += 1
    # move to the next child node  
    t = t.child[char]
  # mark as end of word  
  t.is_end_of_word = True

def disp_node(s:node):
    val =  s.val
    cnt = s.cnt
    is_end_of_word = s.is_end_of_word
    keys = list(s.child.keys())
    print(f"node:{val: >6} cnt:{cnt: >2} word:{is_end_of_word: >1} k:{keys}")
    
def disp_trie(s:node, prefer:int=0):
  t = s
  while True:
    disp_node(t)
    # import pdb;pdb.set_trace()
    if len(t.child.keys()) != 0:
        if len(t.child.keys()) > prefer:
            next = list(t.child.keys())[prefer]
        else:
            next = list(t.child.keys())[0]
        t = t.child[next]
    else:
        return

def disp_trie_dfs(s:node):
    # import pdb;pdb.set_trace()  
    t = s
    if t.val == None:
      return
    print(t.val, end=",")
    if t.is_end_of_word:
        print("\n")
    ll = list(t.child.keys())
    for k,v in enumerate(ll):
        disp_trie_dfs(s.child[v])

def disp_trie_bfs(s:node, q:set()):
    #TBD
    pass

    
# main
if __name__ == "__main__":
  print(__file__)
  print(__doc__)

  s = node()
  s.val = "start"
  add(s, "abc")
  add(s, "abort")
  add(s, "aarya")
  add(s, "abba")
  add(s, "abbot")
  add(s, "abbotoir")
  add(s, "aces")
  add(s, "aardvark")
  disp_trie_dfs(s)
  
