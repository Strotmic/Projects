from model.Auto import Auto
from model.Student import Student
from model.Docent import Docent
from model.Persoon import Persoon

#Test je kennis. Verklaar onderstaande code

def test_student():
    print("*********************Test - student*********************")
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "MIT", 1992)
    studenten = [student1, student2, student3]
    print(f"De studenten: {studenten}")

    # zal dit werken & waarom (niet)?
    studenten.sort()
    print(f"Gesorteerd: {studenten}")

    # welke eq-methode wordt hier gebruikt?
    if student1 == student2:
        print("Gelijk")
    else:
        print("Verschillend")


# test_student()


def test_docent():
    print("*********************Test - docent*********************")
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent1.geeft_les_in("MCT")

    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)
    docent2.geeft_les_in("MCT")
    docent2.geeft_les_in("MIT")

    # welke methode wordt hier uitgevoerd?
    print(docent1)
    print(docent2)

    # welke eq-methode wordt hier gebruikt?
    if (docent1 == docent2):
        print("Gelijk")
    else:
        print("Verschillend")


# test_docent()


def werkt_dit():
    print("*********************Werkt dit?*********************")
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)

    # werkt dit? Wat gebeurt er juist?
    print(f"Vereninging: {Docent.vereniging}")
    print(f"Aantal personen: {Student.geef_aantal_personen()}")
    print()

    # wat gebeurt er hier? Verklaar de werking.
    for p in [student1, student2, student3, docent1, docent2]:
        print(f"{p} is {p.leeftijd} jaren oud.")


# werkt_dit()


def test_auto():
    print("*********************Test - auto*********************")
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)

    auto1 = Auto("1-HOW-125", docent1)
    auto2 = Auto("1-SWC-123", docent2)
    auto3 = Auto("1-LAP-945", student1)

    #Verklaar waar in onderstaande code polymorfisme toegepast wordt 
    print("Dit zijn de verschillende voertuigen met hun eigenaars: ")
    for auto in [auto1, auto2, auto3]:
        print(auto)


# test_auto()
