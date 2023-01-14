verzameling1 = [12, 45, -9, -15]
verzameling2 = [12.23, 45.1, 9.478, 15.125, -3.14]
verzameling3 = ["Stijn", "Lies", "Henk"]

def geef_info_list(x:list):
    for i in x:
        print(f'{i} staat op positie {x.index(i)}')

if __name__ == '__main__':
    geef_info_list(verzameling3)