def nsm(txt,ptn):
    n= len(txt)
    m=len(ptn)
    
    l=[]
    
    for i in range (n-m+1):
        
        for j in range (m):
            if txt[j+i]!=ptn[j]:
              break
        
        if(j==m-1):
            l.append(i)
            
    return l


txt="AABBACDNAABA"
ptn="AABA"

print (" the nsm pattern is at indices", nsm(txt,ptn))