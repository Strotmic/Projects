from datetime import datetime
def toon_boodschap(naam):
    uur = datetime.now()
    uur = int(uur.strftime("%H"))
    if uur>=7 and uur<12:
        return(f'Goedemorgen {naam}')
    elif uur >=12 and uur<13:
        return(f'Joepie het is middag {naam}')
    elif uur>=13 and uur<17:
        return(f'{naam} goede nammidag')
    elif uur>=17 and uur<21:
        return(f'{naam} Goede avond') 
    else:
        return(f'Slaapwel {naam}')

if __name__ == '__main__':
    naam = (input('Geef uw naam op: '))
    print(f'{toon_boodschap(naam)}')