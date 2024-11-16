# Community Detection 
>This project helps the user to find the community based on given node in large socail network without disturbing the network structure.It also help the user to how closes person's community or in other words we say that how many person know the given person (node). this is powerfull tool to understand the behaviour of the person. This tool also helps the user to identify the number of community which are so closed to each other in given socail network. We used Leader Based Community Detection Algorithm which was explain in paper[1].To find the Follower we measure the Jaccard similarity [1] which was explain in the paper.

## How to use 
1. Install all the requirement for packages
2. Import networkx library
3. [Dowanload](https://github.com/sp589/project1.git) the packages 
4. Import and directly use the package

## What's special
- You can easly use the packages 
- It give user better control find to leader's community size 
- User define the thershold value that is effect the community size 
- Thershold value varies from 0 to 1, 0 means largest community form by leader and 1 means smallest community form by leader

## Profile
- Author: sunil patel
- Github: [@sp589](https://github.com/sp589/project1.git)
- Project: project1

## Code 
```python
# user know the leader node of graph
from src.Community_detection import module1 as lbcd
import networkx as nx
Graph = nx.karate_club()
# make copy of graph
Gr=graph.copy()
leader = 0
thershold_value = 0.07
community=lbcd.Community_dectection(Gr,leader,thershold_value)
```
or this
```python
# user know the leader node of graph but not give the thershold_value
from src.Community_detection import module1 as lbcd
import networkx as nx
Graph = nx.karate_club()
# make copy of graph
Gr=graph.copy()
leader = 0
#thershold_value = 0.07
community=lbcd.Community_dectection(Gr,leader)
```
or this

```python
# user do not know the leader node of graph give the thershold_value
from src.Community_detection import module1 as lbcd
import networkx as nx
Graph = nx.karate_club()
# make copy of graph
Gr=graph.copy()
#leader = 0
#thershold_value = 0.07
community=lbcd.Community_dectection(Gr)
```
## References
[1] Akachar E, Bougteb Y, Ouhbi B, Frikh B. LeaDCD: Leadership concept-based method for community detection in social networks. Information Sciences. 2025 Jan 1;686:121341.
[1](https://doi.org/10.1016/j.ins.2024.121341)
