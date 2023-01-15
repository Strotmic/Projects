def voeg_nieuw_element_toe(key,value, dic):
    if key in dic.keys():
        return f'Key: {key} already used'
    else:
        dic[key] = value
        return f'{key} succesvol toegevoegd met value: {value}'
    
howest = {}

print(voeg_nieuw_element_toe('1IPO',51,howest))
print(voeg_nieuw_element_toe('1IPO',10,howest))
