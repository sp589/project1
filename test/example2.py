import zipfile
import networkx as nx
from Community_detection import Module1 as lbcd
zf=zipfile.ZipFile("Dataset/football.zip")
txt=zf.read('football.txt').decode()
gml=zf.read('football.gml').decode()
gml=gml.split('\n')[1:]
G=nx.parse_gml(gml)
graph=G.copy()
res=lbcd.Community_dectection(graph,"California",0.05)
print(res)
