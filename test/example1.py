import networkx as nx
from project import module1 as lib1
G=nx.karate_club_graph()
graph=G.copy()
#res=Leader_Based(graph,0.07)
res=lib1.Community_dectection(graph,0,0.07)
print(res)
