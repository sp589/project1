import networkx as nx
from Community_detection import module1 as lbcd
G=nx.karate_club_graph()
graph=G.copy()
res=lbcd.Community_dectection(graph,0,0.07)
print(res)
