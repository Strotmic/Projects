list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
def geef_even_posities(l):
    x=[]
    for i in range(0,len(l),2):
        x.append(l[i])
    return x


print(f"De elementen uit {list1} op de even posities zijn: {geef_even_posities(list1)}")
