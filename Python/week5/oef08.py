evaluaties = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

x = input('Geef een score op: ').upper()
while x!='':
    evaluaties[x] +=1
    x = input('Geef een score op: ').upper()

for i in evaluaties.keys():
    print(f'score: {i} -> aantal: {evaluaties[i]}')
print("Geef de verschilleden evaluatiecijfers door (sluit af met lege waarde)")
print("Uitmuntend: A, Zeer goed: B, Goed: C, Voldoende: D, Onvoldoende: E, Zwak: F")
