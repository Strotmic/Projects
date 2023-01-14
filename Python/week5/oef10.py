mijn_team = {"Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
             "Christophe": ["USA", "Frankrijk", "Duitsland"],
             "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
             "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]}

gezocht_land = input("Geef een land op:> ")

def filter_op_land(dic, land):
    ret =[]
    for i in dic.keys():
        print(dic[i])
        if land in dic[i]:
            ret.append(i)
    return ret

print(f"Deze personen hebben reeds dit land bezocht: {filter_op_land(mijn_team,gezocht_land)}")
