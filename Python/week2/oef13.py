def geef_celcius(graden):
    temp = (graden - 32) * 5 / 9 
    return round(temp,2)

def geef_fahrenheit(graden):
    rtemp = (graden * 9 / 5) + 32 
    return round(rtemp,2)

if __name__ == '__main__':
    omzetting = (input('Welke eenheid wilt u gebruiken C:Celcius, F:Farenheit: '))

    if omzetting == 'C':
        graden = float(input('Geef een temperatuur op in celcius: '))
        print(f'De overeenkomstige temp in farenheit is {geef_fahrenheit(graden)}')
    else:
        graden = float(input('Geef een temperatuur op in farenheit: '))
        print(f'De overeenkomstige temp in celcius is {geef_celcius(graden)}')
    