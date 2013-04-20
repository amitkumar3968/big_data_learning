import pygraphviz as pgv
import networkx as nx
import itertools as it
from networkx.algorithms import bipartite

def is_planar(G):
    """
    function checks if graph G has K(5) or K(3,3) as minors,
    returns True /False on planarity and nodes of "bad_minor"
    """
    result=True
    bad_minor=[]
    n=len(G.nodes())
    if n>5:
        for subnodes in it.combinations(G.nodes(),6):
            subG=G.subgraph(subnodes)
            if bipartite.is_bipartite(G):# check if the graph G has a subgraph K(3,3)
                X, Y = bipartite.sets(G)
                if len(X)==3:
                    result=False
                    bad_minor=subnodes
    if n>4 and result:
        for subnodes in it.combinations(G.nodes(),5):
            subG=G.subgraph(subnodes)
            if len(subG.edges())==10:# check if the graph G has a subgraph K(5)
                result=False
                bad_minor=subnodes
    return result,bad_minor

#create random planar graph with n nodes and p probability of growing
n=8
p=0.6
while True:
    G=nx.gnp_random_graph(n,p)
    if is_planar(G)[0]:
        break
#visualize with pygraphviz
A=pgv.AGraph()
A.add_edges_from(G.edges())
A.layout(prog='dot')
A.draw('planar.png')
