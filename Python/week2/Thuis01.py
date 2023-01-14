def kassa(broek,tshirt,vest):
    return(f'*** welkom bij het kassasysteem ***\nU kocht:\n\tBroeken: {broek} stuks(s) \n\tT-Shirts: {tshirt} stuk(s)\n\tVesten: {vest} stuk(s) \nTotaal te betalen: {broek* 70.5+20.89*tshirt+100.3*vest}')

if __name__ == '__main__':
    broek = int(input('Hoeveel broeken werden er gekocht? '))
    tshirt = int(input('Hoeveel T-shirts werden er gekocht? '))
    vest = int(input('Hoeveel vesten werden er gekocht? '))
    print(kassa(broek,tshirt,vest))

