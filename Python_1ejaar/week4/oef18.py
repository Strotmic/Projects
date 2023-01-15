from re import S


brutowedde_arbeider = []
brutowedde_bediende = []
brutowedde_kader = []

brutowedde_na_inlevering_arbeider = []
brutowedde_na_inlevering_bediende = []
brutowedde_na_inlevering_kader = []

def werknemers_loon(x,y):
    d={'A':0.05,'B':0.08,'K':0.1}
    for i in d.keys():
        if i == x:
            return y*d[i]

lengte = int(input('Geef het aantal werknemers op: '))
for i in range(lengte):
    type = input("Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > ")
    bruto = float(input('Geef brutoloon op: '))
    if type == 'A':
        brutowedde_arbeider.append(bruto)
    elif type == 'B':
        brutowedde_bediende.append(bruto)
    else:
        brutowedde_kader.append(bruto)

s = 0
for i in ((brutowedde_arbeider)):
    print(f'A\t{i} -> {i - werknemers_loon("A",i)}')
    s+=werknemers_loon("A",i)
for i in ((brutowedde_bediende)):
    print(f'B\t{i} -> {i - werknemers_loon("B",i)}')
    s+=werknemers_loon("B",i)
for i in ((brutowedde_kader)):
    print(f'K\t{i} -> {i - werknemers_loon("K",i)}')
    s+=werknemers_loon("K",i)

totaal  = sum(brutowedde_kader)+sum(brutowedde_arbeider)+sum(brutowedde_bediende)
print(f'Aantal werknemers: {lengte} \nAantal arbeiders {len(brutowedde_arbeider)}\nAantal bedienden {len(brutowedde_bediende)}\nAantal kaderpersoneel: {len(brutowedde_kader)}\nTotaal brutoloon: {totaal}\nTotaal loon na inlevering {totaal-s} \nTotaal bedrag {s}')
print(f'')



