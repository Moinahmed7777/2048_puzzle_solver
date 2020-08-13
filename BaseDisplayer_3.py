
class BaseDisplayer:
    def __init__(self):
        pass

    def display(self, grid):
        pass
'''
c_l=[]
def check(c_l,n_l):
    T_count=0
    T_table=0
    #Tlen=len(c_l)
    
    for k in range(len(c_l)):
        c2_l=c_l[k]
        
        #print(c2_l)
    
    
        for i in range(len(n_l)):
            for j in range(len(n_l)):
                if n_l[i]==c2_l[j]:
                    T_count+=1
                    break
        
        if not T_count==4:
            T_table+=1
        T_count=0
    if T_table==len(c_l):
        c_l.append(n_l)
    
X=[[-4, -5, -2, -3], [-4, -5, -3, -2], [-4, -5, -3, -2], [-4, -5, -5, 0],[-2, -5, -5, -2], [-2, -5, -3, -4], [-2, -5, -2, -5]]
lk=0
for h in range(len(X)):
    if h==0:
        c_l.append(X[h])
        #print(c_l)
    else:
        lk+=1
        #print(lk)
        check(c_l,X[h])

print(c_l)

def Remove(lst): 
     return ([list(i) for i in {*[tuple(sorted(i)) for i in lst]}])   
       
# Driver code 
lst=X
print(Remove(lst)) 


for _, set in enumerate([11,12,13,14]):
    print("_",_,"set",set)
'''