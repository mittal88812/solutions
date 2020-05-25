def toys(w):
    result=[]
    w.sort()
    while(len(w)>0):
        li=[]
        l=len(w)
        mi=w[0]
        up=mi+4
        for x in range(l):
            if w[x]<=up:
                li.append(w[x])
                c=x
            else:
                break
        result.append(li)
        if(c==(l-1)):
            break
        else:
            w=w[c+1:]
//    print(result)
    return(len(result))






//  for problem statement visit:https://www.hackerrank.com/challenges/priyanka-and-toys/problem?h_r=internal-search
