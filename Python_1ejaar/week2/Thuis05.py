def stopafstand(weer,snelheid,reactietijd):
    if weer == 'N':
        return(((snelheid/3.6)*reactietijd)+((snelheid/3.6)**2)/(2*5))
    else:
        return(((snelheid/3.6)*reactietijd)+((snelheid/3.6)**2)/(2*8))

if __name__ == '__main__':
    snelheid = float(input('Geef de snelheid op '))
    weer = input('Welk weer is het Nat:N en Droog:D ')
    reactietijd = float(input('Geef de reactitijd op in seconden: '))
    print(stopafstand(weer,snelheid,reactietijd))
