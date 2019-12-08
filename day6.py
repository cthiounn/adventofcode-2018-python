import sys
from collections import Counter
with open('data/my_input/6.in','r') as f:
    lines=[l.strip() for l in f]

def part1(l):
    d=dict()
    for a in l:
        x,y=map(int,a.split(','))
        d[(x,y)]= (x,y)
    xc=[a[0] for a in d.keys()]
    yc=[a[1] for a in d.keys()]
    xmin=min(xc)
    xmax=max(xc)
    ymin=min(yc)
    ymax=max(yc)
    m=dict()
    safe=0
    for i in range(xmin,xmax):
        for j in range(ymin,ymax):
            if (i,j) not in m :
                lis=[(e,dman(e,(i,j))) for e in d  ]
                lis2=[v for k,v in lis]
                if sum(lis2)<10000:
                    safe+=1
                lis=sorted(lis,key=lambda p:p[1],reverse=True)
                k,v=lis.pop()
                k2,v2=lis.pop()
                if v<v2:
                    m[(i,j)]=k
    unwanted=[v for k,v in m.items() if k[0]==xmin or k[0]==xmax or k[1]==ymax or k[1]==ymin  ]
    unwanted=set(unwanted) #change type for uniqueness
    print(max(Counter([v for v in m.values() if v not in unwanted]).values()))
    print(safe)

def dman(a,b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

part1(lines)