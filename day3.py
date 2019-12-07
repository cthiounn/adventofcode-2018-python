import re
with open('data/my_input/3.in','r') as f:
    lines=[line.strip() for line in f]

def part1(l): 
    d=dict()
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), l)
    unpure=set()
    allidt=set()
    for idt,x,y,i,j in claims:
        allidt.add(idt)
        for l in range(i):
            for k in range(j): 
                if (x+l,y+k) in d:
                    if idt  not in unpure:
                        unpure.add(idt)
                    if d[(x+l,y+k)]  not in unpure:
                        unpure.add(d[(x+l,y+k)])
                    d[(x+l,y+k)]='#'
                else:
                    d[(x+l,y+k)]=idt
    print(len([1 for a,b in d if d[a,b]=="#"])) 
    print(allidt-unpure)
    
 

part1(lines)
# part2(lines)