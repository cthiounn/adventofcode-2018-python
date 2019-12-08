with open('data/my_input/5.in','r') as f:
    line= [l.strip() for l in f]

def part1(l):
    ml=[]
    ab=" abcdefghijklmnopqrstuvwxyz"
    for a in ab:
        s=l[0].replace(a,'').replace(a.upper(),'')
        p=['-']    
        for c in s:
            c1=p[-1]
            if c1.lower()==c.lower() and c1!=c:
                p.pop()
            else:
                p.append(c)
        if a==" ":
            print(len(p)-1)
        else:
            ml.append(len(p)-1)
    print(min(ml))

part1(line)