# # # # from math import pi
# # # # import math
# # # # print(dir(math))

# # # import sys

# # # print(f'De gebruikte vesie van Pytohn is {sys.version}')

# # import datetime


# # print(f'De huide datum en tijd is {datetime.datetime.now()}')

# from math import pi

# x  = float(input('Geeef de straal van een cirkel op.'))
# print(f'De straal van de cirkel is {pi * x**2}')

# from calendar import prmonth
# x = int(input('maand'))
# y=int(input('jaar'))

# print(prmonth(y, x, w=0, l=0))

import multiprocessing

print(multiprocessing.cpu_count())
