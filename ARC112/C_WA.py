class node:
  def __init__(self):
    self.parent = -1
    self.children = []
    self.type = ""
    self.depth = 0
    
def cal_depth(parent, d = 1):
  tree[parent].depth = d
  # print(tree[parent].depth)
  # print(tree[parent].children)
  for child in tree[parent].children:
    cal_depth(child, d+1)
    
n = int(input())
tree = [node() for _ in range(n)]
tree[0].type = "root"
nodes = list(map(int, input().split()))
count = 1

for i in range(n-1) :
  if i+2 in nodes :
    children = [j for j, x in enumerate(nodes) if x == i+2]
    tree[nodes[i]-1].children = children
    # print(tree[nodes[i]].children)
    tree[nodes[i]-1].type = "internal node"
  else :
    tree[nodes[i]-1].type = "leaf"
    
  for child in tree[nodes[i]-1].children:
    tree[child].parent = nodes[i]-1
    # print(tree[child].parent)

cal_depth(0)

depth_list = []
for node in tree :
  depth_list.append(node.depth)
depth_list.sort()
max_depth = depth_list[-1]
second_largest_depth = depth_list[-2]
    
if n % 2 == 0 :
  count += max_depth
else :
  count += second_largest_depth-1
print(count)