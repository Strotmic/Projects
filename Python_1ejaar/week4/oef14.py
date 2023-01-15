list_getallen1 = [78, 4, 5, 6, 4]
list_getallen2 = [89, 78, 4]
x=['a','b','c']
y=['a','b','d']
print(f"List1: {list_getallen1} ")
print(f"List2: {list_getallen2} ")

def geef_gemeeschappelijke_elementen(l,l2):
    x=l+l2
    ret=[]
    for i in x:
        if x.count(i)>1:
            ret.append(i)
    return list(set(ret))

print(geef_gemeeschappelijke_elementen(x,y))

