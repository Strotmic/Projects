score= float(input('Geef een score op: '))

import math
# if round(score)>=10:
#     print(f'U bent geslaagd met een score van {round(score)}')
# else:
#     print(f'U bent niet geslaagd {round(score)}')

komma = score - int(score) 

if komma >= .5:
    score = math.ceil(score)
else:
    score = math.floor(score)
if score>=10:
     print(f'U bent geslaagd met een score van {(score)}')
else:
     print(f'U bent niet geslaagd {(score)}')

