from model.OuderRepository import OuderRepository

def test_json():
    list_ouders = OuderRepository.inlezen_ouders_met_studenten()
    for ouder in list_ouders:
        ouder.geef_info_studenten()
        print('\n')
    
    print("Lijst van ouders met de opleidingen die hun kinderen volgen:")
    for ouder in list_ouders:
        print(f"De kinderen van {ouder} volgen deze opleidingen: {ouder.geef_opleidingen_studenten()}")   

    naam_opleiding = input("\nGeef een opleiding op:> ")
    list_resultaat = OuderRepository.filter_ouders_met_studenten_uit_opleiding(list_ouders,naam_opleiding)
    print("Resultaat zoekopdracht: ")
    for ouder in list_resultaat:
        print(f"{ouder} heeft {len(ouder.studenten)} student(en) die de opleiding {naam_opleiding} volgen.")

test_json()