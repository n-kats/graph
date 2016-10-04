# see http://qiita.com/shimo_t/items/b761973805f2cf0b2967
from graphviz import Digraph

G = Digraph(format="png")
G.attr("node", shape="circle")

N = 15
for i in range(N):
	G.node(str(i), str(i))

for i in range(N-1):
	G.edge(str(i//2), str(i+1))
print(G)
G.render('binary_tree')
