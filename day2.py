from collections import Counter
with open('data/my_input/2.in','r') as f:
    li=[line.strip() for line in f]

def part1(l):
    double=[ 1 for s in l if any( d==2 for d in Counter(s).values())]
    triple=[ 1 for s in l if any( d==3 for d in Counter(s).values())]
    print(        sum(double)*sum(triple)    )

def part2(l):
    for s in l:
        for s2 in l:
            if (s==s2):
                continue 
            if len([1 for i,j in list(zip(s,s2))  if i!=j])==1:
                print("".join([ i for i,j in list(zip(s,s2)) if i==j]))

part1(li)
part2(li)