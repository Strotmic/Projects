from model.Personenwagen import Personenwagen
from model.PersonenwagenRepository import PersonenwagenRepository
from typing import List

def print_info(lst_personenwagens: List[Personenwagen]) -> None:
    for auto in lst_personenwagens:
        print(f"{auto.id} - {auto} - heeft {auto.max_aantal_zitplaatsen} plaatsen / {auto.aantal_personen} passagiers aan boord-> {auto.vrije_plaatsen} vrije plaatsen")


print("****start inlezen****")
beschikbare_taxis = PersonenwagenRepository.inlezen_personenwagens()
print("****inlezen is voltooid****")
input_gebruiker = input("Wat wil je doen? [o]verzicht, [p]assagier ingeven > ")
while input_gebruiker != "":
    if input_gebruiker.upper() == "O":
        print_info(beschikbare_taxis)
    elif input_gebruiker.upper() == "P":
        try:
            temp_id = input("Geef het ID van de taxi > ")
            temp_pers = int(input("Hoeveel personen stappen er in? > "))
            temp_wagen = PersonenwagenRepository.zoek_wagen(
                beschikbare_taxis, temp_id)
            temp_wagen.aantal_personen = temp_pers
        except Exception as ex:
            print(f"Fout: {ex}")

    input_gebruiker = input("Wat wil je doen? [o]verzicht, [p]assagier ingeven > ")
