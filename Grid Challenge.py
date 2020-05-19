def gridChallenge(grid):
    l=len(grid)
    new=[]
    for x in range(l):
        l=split(grid[x])
        new.append(l)
    new1=[]
    for x in new:
        x.sort()
        new1.append(x)
    li=[]
    for x in range(len(new1[0])):
        t=[]
        for y in range(len(new1)):
            t.append(new1[y][x])
        li.append(t)
    li1=[]
    for x in range(len(new1[0])):
        t=[]
        for y in range(len(new1)):
            t.append(new1[y][x])
        li1.append(t)
    for x in li:
        x.sort()
    c=1
    for x in range(len(li)):
        if(li[x]!=li1[x]):
            c=0
            break
        else:
            pass
    if(c==1):
        return("YES")
    else:
        return("NO")




//for problem statement visit:https://www.hackerrank.com/challenges/grid-challenge/problem
