import re
import operator

with open('data/my_input/4.in','r') as f:
    lines=[l.strip() for l in f]

def part1(l):
    num=lambda s : re.findall('\d+',s)
    d=dict()
    sleepSchedule=dict()
    lastevent=[]
    idg=0
    for ll in map(num,sorted(l)):
        ll=list(map(int,ll))
        if len(ll)==6:
            idg=ll.pop()
            continue
        elif lastevent:
            
            for i in range(lastevent[4],ll[4]):
                sleepSchedule[(idg,i)]=1 if (idg,i) not in sleepSchedule else sleepSchedule[(idg,i)]+1 
            d[idg]=list(map(operator.sub,ll,lastevent))[4] if idg not in d else d[idg]+list(map(operator.sub,ll,lastevent))[4]
            lastevent=[]
        else:
            lastevent=ll
    sleepy=max(d.items(),key=lambda x:x[1])
    time=[(t,sleepSchedule[(idg,t)]) for idg,t in sleepSchedule if idg==sleepy[0]]
    alltime=[(idg,t,sleepSchedule[(idg,t)]) for idg,t in sleepSchedule]
    answer2=max(alltime,key=lambda x:x[2])
    print(sleepy[0]*max(time,key=lambda x:x[1])[0]) 
    print(answer2[0]*answer2[1])

part1(lines)