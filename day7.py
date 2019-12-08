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
part1(lines)
