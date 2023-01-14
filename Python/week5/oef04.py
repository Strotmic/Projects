print("Dictionary ....")
print("Key: .... -> value: ....")
mit ={"1MIT": 58, "2MIT": 36}
mct={"1MCT": 131, "2MCT": 88, "3MCT": 77}
devine={"1Devine": 123, "2Devine": 98, "3Devine": 55}

def print_dictionary(name,dic):
    print(f'Verzameling {name}')
    for i in dic.keys():
        print(f'key {i} met value: {dic[i]}')

print_dictionary('Devine',devine)

