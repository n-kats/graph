# see http://qiita.com/shimo_t/items/b761973805f2cf0b2967
from graphviz import Digraph

G = Digraph(format="png")
G.attr("node", shape="circle")

D = 4
N = 2**D -1
for i in range(N):
	if i == 0:
		label = "root"
	elif i>=2**(D-1)-1:
		label = "class%d" % (i-2**(D-1)+1)
	else:
		label = ""
	G.node(str(i), label=label)
G.node
for i in range(N-1):
	k = i//2
	if i % 2 == 0:
		label = "p[%d]" % k
	else:
		label = "1-p[%d]" % k

	G.edge(str(i//2), str(i+1), label=label)
print(G)
G.render('pic_hiercy')
