sec = float(input('Geef het aantal seconden op?'))

dagen = (sec//86400)
uren = ((sec-dagen*86400)//3600)
minuten = (((sec-(dagen*86400)-(uren*3600))//60))
seconden = (sec - (dagen*86400) - (uren*3600) - (minuten *60))

print(f'd:h:m:s -> {dagen}:{uren}:{minuten}:{seconden}')




