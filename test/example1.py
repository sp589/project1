import networkx as nx
G=nx.karate_club_graph()
graph=G.copy()
#res=Leader_Based(graph,0.07)
res=lib1.Community_dectection(graph,0,0.04)
print(res)
