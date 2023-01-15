def vertaal_maandnummermer_naar_str(nummer):
    if nummer <1 or nummer>12:
        return 'De overkomstige maand is onbekend'
    if nummer == 1:
        return("De maand is Januari")
    elif nummer == 2:
        return("De maand is Februari")
    elif nummer == 3:
        return("De maand is Maart")
    elif nummer == 4:
        return("De maand is April")
    elif nummer == 5:
        return("De maand is Mei")
    elif nummer == 6:
        return("De maand is Juni")
    elif nummer == 7:
        return("De maand is Juli")
    elif nummer == 8:
        return("De maand is Augustus")
    elif nummer == 9:
        return("De maand is September")
    elif nummer == 10:
        return("De maand is Oktober")
    elif nummer == 11:
        return("De maand is November")
    elif nummer == 12:
        return("De maand is December")

if __name__ == '__main__':
    maand = int(input('Geef een maandnummer op: '))
    print(vertaal_maandnummermer_naar_str(maand))