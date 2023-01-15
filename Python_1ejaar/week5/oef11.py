mijn_team = {"Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
             "Christophe": ["USA", "Frankrijk", "Duitsland"],
             "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
             "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]}

def geef_populariet_landen(dic):
    ret = {}

    for i in dic.keys():
        for j in (dic[i]):
            if j in ret.keys():
                ret[j] +=1
            else:
                ret[j] =1

    return ret

lijst = geef_populariet_landen(mijn_team)
for i in lijst.keys():
    print(f'Land: {i} -> aantal: {lijst[i]}')
