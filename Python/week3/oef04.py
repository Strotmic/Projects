s=''
for i in range(10, 129):
    if i %2==0:
        pass
    else:
        s += f'{i}, '
print(s[:-2])