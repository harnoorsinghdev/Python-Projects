

dictOFMARKS={200:('Name 1','Section a','2018','Python'),100:('Name 2','Section B','2019','English'),80:('Name 3','Section a','2018','Python'),90:('Name 4','Section B','2017','Python')}
lenn=len(dictOFMARKS)
def sum():
    sum1=0
    i=0
    for k in dictOFMARKS.keys():
        sum1=sum1+k
        i=i+1
        if(i==lenn):
            return sum1
        
def avg():
    avg1=0
    
    for k in dictOFMARKS.keys():
        sum1=sum()
        return sum1/lenn
        
def high():
    high=0
    for k in dictOFMARKS.keys():
        if(k>high):
            high=k
        return high    
        
out=sum()
print("sum is",out)

avgg=avg()
print("average is",avgg)
        
highest=high()
print("highest is",highest)
