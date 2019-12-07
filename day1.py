with open('data/my_input/1.in','r') as f:
    numbers= [line.strip() for line in f]

def part1(l):
    print(sum(map(int,l)))

def part2(l):
    seen=dict()
    sum=0
    stop=False
    while not stop:
        for i in l:
            sum+=int(i)
            if sum in seen:
                print(sum)
                stop=True
                break
            seen[sum]=1

part1(numbers)
part2(numbers)