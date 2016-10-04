from graphviz import Digraph

g = Digraph('G', filename='gv/hello.gv')
g.edge('Hello', 'World')

