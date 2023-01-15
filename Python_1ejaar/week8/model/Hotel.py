from model.Hotelgast import *

class Hotel:
    def __init__(self, naam, gastenlijst=[]) -> None:
        self.naam = naam
        self.__gastenlijst = gastenlijst
    
    def check_in(self,naam,voornaam):
        gast = Hotelgast(naam,voornaam)
        if len(self.gastenlijst) ==0:
            self.gastenlijst.append(gast)
            gast.is_ingecheckt =True
            print(f'Correct ingecheckt: \n{gast}')
        else:
            for i in self.gastenlijst:
                if i == gast:
                    print( f'Sorry deze gast bestaat al.')
                    break
                else:
                    self.gastenlijst.append(gast)
                    gast.is_ingecheckt =True
                    print( f'Correct ingecheckt: \n {gast}')
                    break

    def print_info_gasten(self):
        print(f'Dit zijn de aanwezige gasten in hotel {self.naam}')
        for i in self.gastenlijst:
            print(i)

    def __zoek_hotelgast(self,naam,voornaam):
        voorlopig = Hotelgast(naam,voornaam)
        for i in self.gastenlijst:
            if i == voorlopig:
                return i
        return 'None'
    
    def check_out(self,naam,voornaam):
        gast = self.__zoek_hotelgast(naam,voornaam)
        if type(gast) == type('None'):
            print( f'Deze gast ({naam} {voornaam}) bestaat niet')
            return gast

        else:
            if gast.saldo == 0:
                self.gastenlijst.remove(gast)
                print( f'Correct uitgecheckt:OK: {gast.naam} - {gast.saldo} euro')
                return gast
            else:
                print( f'Deze persoon ({naam} {voornaam}) heeft geen saldo 0')

    def bestel_drank(self,naam,voornaam,drank):
        gast = self.__zoek_hotelgast(naam,voornaam)            
        if type(gast) == type('None'):
            print( f'Deze gast ({naam} {voornaam}) bestaat niet')
        else: 
            drank = float(drank)
            gast.saldo += drank

    def vereffen_saldo_gast(self,naam,voornaam):
        gast = self.__zoek_hotelgast(naam,voornaam)            
        if type(gast) == type('None'):
            print( f'Deze gast ({naam} {voornaam}) bestaat niet')
        else: 
            gast.saldo =0

    def __str__(self) -> str:
        return f'Hotel:{self.naam}'


    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value: str) -> None:
        if value =='':
            print('Foutieve naam')
        else:
            self.__naam = value

    # ********** property gastenlijst - (enkel getter) ***********
    @property
    def gastenlijst(self) -> list:
        """ The gastenlijst property. """
        return self.__gastenlijst
    
    
    
    
    
