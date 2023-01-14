test = ["A", 89, 78, 4, "A", "test", 4]

def verwijder_dubbels(l):
    return list(set(l))

print(f"{test}\nZonder dubbels: {verwijder_dubbels(test)}")
