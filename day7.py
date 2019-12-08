import sys
import networkx as nx 
import re
with open('data/my_input/7.in','r') as f:
    lines=[l.strip() for l in f]

def part1(l):
    d=nx.DiGraph()
    for li in l:
        x,y,z=re.findall('[A-Z]',li)
        d.add_edge(y,z)
    print(''.join(nx.lexicographical_topological_sort(d)))

    seconds=0
    nodes_in_progress=dict()
    while(d.nodes()):
        finished_nodes=[]
        for n1 in nodes_in_progress:
            nodes_in_progress[n1]+=-1
            if nodes_in_progress[n1]==0:
                d.remove_node(n1)
                finished_nodes.append(n1)
        for fi in finished_nodes:    
            del nodes_in_progress[fi]
        nodes_available=[n for n,d in d.in_degree() if d==0] 
        for nn in sorted(nodes_available):
            if len(nodes_in_progress)<5 and nn not in nodes_in_progress:
                nodes_in_progress[nn]=60+ord(nn)-64
        seconds+=1
    print(seconds-1)

part1(lines)
