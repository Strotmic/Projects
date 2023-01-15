def exclusief_naar_inclusief(exl,btw):
    return exl*btw

if __name__ == '__main__':
    exl = float(input('Geef een bedrag exl btw op?: '))
    btw = float(input('Geef een btw percentage op: '))
    print(f'Het totaal bedrag inc btw is {exclusief_naar_inclusief(exl,btw)}')
    