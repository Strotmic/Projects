def get_bedrag(type,dagen,kilometers):
    tot = 0
    if type=='A':
        tot += dagen * 25
        tot += kilometers * 0.5
    elif type=='B':
        tot += dagen * 35
        tot += kilometers * 0.6
    else:
        tot += dagen * 45
        tot += kilometers * 0.7
    return tot

A_autos = 0
B_autos = 0
C_autos = 0

A_km = []
B_km = []
C_km = []

while True:
    type = input('Wat is het type van de auto A,B of C: ').upper()
    if type == '':
        break
    dagen = int(input('Hoeveel dagen: '))
    kilometers = float(input('Hoeveel kilometers: '))

    if type == 'A':
        A_autos += get_bedrag(type,dagen,kilometers)
        A_km.append(kilometers)
    elif type == 'B':
        B_autos += get_bedrag(type,dagen,kilometers)
        B_km.append(kilometers)
    else:
        C_autos += get_bedrag(type,dagen,kilometers)
        C_km.append(kilometers)

print(f'Bedragen:\nAuto A {A_autos}\nAuto B {B_autos}\nAuto C {C_autos}')
print(f'Totaal aantal autos\nAutos A {len(A_km)}\nAutos B {len(B_km)}\nAuto C {len(C_km)}')
print(f'Totaal aantal gereden van kms \nAuto A {sum(A_km)}\nAuto B {sum(B_km)}\nAuto C {sum(C_km)}')


