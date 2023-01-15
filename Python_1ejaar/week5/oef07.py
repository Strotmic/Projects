import re

def tel_voorkomen_woorden(x):
    x = re.sub('[,?!.]','',x)
    x=x.split()
    res = {}
    for i in x:
        if i in res.keys():
            res[i] +=1
        else:
            res[i] =1
    return res
zin = "Dit is Howest, is het niet zo? Uiteraard, welkom!"
print(f"Onderzochte zin:\n{zin}\n")
dic_woorden = tel_voorkomen_woorden(zin)
for i in dic_woorden.keys():
    print(f'key: {i} -> value: {dic_woorden[i]}')
