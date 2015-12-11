'''
Contains data structures and meathods for their use:
General Meathods
  - get_search_score(data, match) returns float representing how closely it matches
linked_list
  - find (linked_list, data) returns top node matching that perametter
  - find_all(linked_list, data) returns all nodes mathcing that data
  - find_within_math(linked_list, data, match) find all nodes matching at;east 1-match with the data
'''

# Simple linked list for storing data
class linked_list:
  count = 0
  def __init__(self, previous, nxt, data):
    self.ident = linked_list.count
    linked_list.count += 1
    self.prev = previous
    self.nxt = nxt
    self.data = data
  def save(self, ll):
    node = ll
    while node.prev != 0:
      node = node.prev
    s = ""
    while node != 0:
      s += node.data + '\n'
      node = node.nxt
    return s
  def load(self, s):
    node = linked_list(0, 0, s.split('\n')[0])
    init_node = node
    for i in s.split('\n')[1:]:
      new_node = linked_list(node, 0, i)
      node = new_node
    return init_node
  def append_new(self, data):
    node = self
    while node.prev != 0:
      node = node.prev
    node.prev = linked_list(0, node, data)

lis = linked_list(0, 0, "Hello")

class awt_tree:
  count = 0
  def __init__(self,parent, data):
    self.ident = count
    count += 1
    self.patent = parent
    self.data = data
    self.right = 0
    self.left = 0
  def add_node(self,data):
    if compare(self.data, data) > 0:
      if self.right == 0:
        node = awt_tree(self, data)
        self.right = node
        return node
      else:
        return self.right.add_node(data)
    else:
      if self.left == 0:
        node = awt_tree(self, data)
        self.left = node
        return node
      else:
        return self.left.add_node(data)
    def find(self, data):
      if self.data == data:
        return this
      else:
        if compare(self.data, data) > 0:
          if self.right == 0:
            return 0
          else:
            return self.right.find(data)
        else:
          if self.left == 0:
            return 0
          else:
            return self.left.find(data)

def compare(data1, data2):
  for i in range(min(len(data1), len(data2))):
    if ord(data1[i]) - ord(data2[i]) != 0:
      return ord(data1[i]) - ord(data2[i])
  return len(data1) - len(data2)

def find(ll, d):
  node = ll
  while node.data != d:
    node = node.nxt
  return node

def find_all(ll, d):
  node = ll
  ret = []
  while node != 0:
    if node == d:
      ret += [node]
    node = node.nxt
  return ret

def find_within_match(ll, d, m):
  ret = []
  node = ll
  while node != 0:
    if get_search_score(ll.data, d) + m >= 1:
      ret += [node]
    node = node.nxt
  return ret

def get_search_score(d, m):
  pointer = 0
  score = 0
  chain = 0
  for i in range(len(m)):
    if m[i] == d[pointer]:
      chain += 1
      pointer += 1
    else:
      score += chain * chain
      chain = 0
      if m[i] in d:
        chain += 1
        pos = pointer
        for u in d[pointer:] + d[:pointer]:
          if u == d[i]:
            break
          pos += 1
        if pos > len(d):
          pos -= len(d)
  score += chain * chain
  return float(score)/float(len(d)*len(d))
