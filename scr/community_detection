#!/usr/bin/env python
# coding: utf-8
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import networkx as nx
from random import randint

def intersection(c,x):
    """ calculate the intersection of two given set 

    Args:
        c (_type_): _description_
        x (_type_): _description_

    Returns:
           _type_: _description_
    """
    return list(set(c) & set(x))
def union(c,x):
        """_summary_

        Args:
            c (_type_): _description_
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        return list(set(c) | set(x))
def Similarity_measure(Gr,leader,person): 
    """
    This fuctaion calculate the similarity between two nodes based on how number of common node between them 
    and give them some vaue between 0 to 1 . The two node's neighbour node are common then the similarity value is high as 1
    if there are no common neighbour between them then similarity is 0. 
    Args:
        Gr (Networx graph): this is the graph 
        leader (Networkx node): node of given graph network of Gr 
        person (Networkx node): node of given graph network of Gr

    Returns:
        float: the similarity between given two node in given network
    """
    k_x = Gr.degree(leader)
    c=[n for n in Gr.neighbors(leader)]
    x=[n for n in Gr.neighbors(person)] 
    lenght_of_common_nodes=len(list(set(c) & set(x))) 
    lenght_of_union=len(list(set(c) | set(x)))
    if (lenght_of_union>0):
        similarity =  lenght_of_common_nodes/ lenght_of_union
    else:
        similarity=0
    return similarity
def leader_selection(Gr):
    """ this funcation gives the most influantial node in given graph network by considering the connection of neighbour'
    neighbours
         Args:
             Gr (Networkx Graph): the graph network 

        Returns:
            Networkx Node: the most imortant node in the graph Network
    """
    centrality=nx.eigenvector_centrality(Gr,max_iter=100000000)
    c_valu_l=list(centrality.values())
    c_node=list(centrality.keys())
    return c_node[c_valu_l.index(max(c_valu_l))]

def check_for_node_left(temp_c,temp_r,Graph):
    """ this funcation search the any node or subgraph in that are completly disconnected by main graph network
    which are form while removing node of known community in graph. 
      
        Args:
            temp_c (list): list of node which are the part of community
            temp_r (list): list of node which are not part of community
            Graph (Networkx Graph) : main graph network

        Returns:
            temp_c (list): list of node which are part of community 
            Graph (Networkx Graph) : Graph after removing the all the node of community
    """
    H=Graph.subgraph(temp_r)
    connected_components_list=list(nx.connected_components(H))
    for i in connected_components_list:
        if (len(i))==1:
            temp_c.append((list(i))[0])
            #temp_r.remove((list(i))[0])
    for node in temp_c:
        Graph.remove_node(node)
    return temp_c,Graph
    
def Leader_Based(Gr,thershold=0.001):
    """ this funcation used to find the community in the entire social network graph

        Args:
            thershold (float) : it resemble the how close community you want it value varies from 0 to 1 and default value is 0.01
            Gr (Networkx Graph) : social Network graph 

        Returns:
            list: list of community 
    """
    community=[]
    community=[]
    temp_c=[]
    temp_r=[]
    while(len(Gr)!=0):
        leader=leader_selection(Gr)
        for i in Gr:
            similarity = Similarity_measure(Gr,leader,i)
            if similarity > thershold: 
                temp_c.append(i)
            else:
                temp_r.append(i)
        com,Gr=check_for_node_left(temp_c,temp_r,Gr)
        community.append(com.copy())
        temp_c.clear()
        temp_r.clear()
    #print("lbcd",len(community))
    return community

def community_show(Graph,community):
    """ this funcation show the graphical repesention of community in a given network in which similar color node represent the similar community 

    Args:
        Graph (Networkx Graph): social network
        community (list): list community 
    """
    import matplotlib.pyplot as plt
    from random import randint
    color = []
    for i in range((len(community))):
        color.append('#%06X' % randint(0, 0xFFFFFF)) 
    nodelist=[n for n in Graph]
    color_map=nodelist.copy()
    for i in range((len(community))):
        for node in Graph:
            if node in community[i]:
                color_map[nodelist.index(node)]=color[i]
    #nx.draw(Graph, node_color=color_map,with_labels=True)
    pos = nx.spring_layout(Graph)
    import warnings
    warnings.filterwarnings('ignore')
    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = (20, 15)
    plt.axis('off')
    nx.draw_networkx(Graph,pos, with_labels = True,node_color=color_map, node_size = 600)
    plt.show()
    
        
