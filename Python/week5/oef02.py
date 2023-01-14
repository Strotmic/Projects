t1=('1MCT1','1MCT2','1MCT3')
t2 = ('1MIT1','1MIT2')

def print_tuple(name,t):
    print(f'Verzameling {name}')
    for i in t1:
        print(f'{i} zit op positie {t1.index(i)}')

print_tuple('MCT',t1)