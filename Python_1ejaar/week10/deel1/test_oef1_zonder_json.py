from model.Auto import Auto
from model.Student import Student
from model.Ouder import Ouder

# LABO


def test_ouder():
    print("*********************Test - auto*********************")
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "MIT", 1992)

    ouder1 = Ouder("Spriet", "Marc", 1951)
    ouder1.voeg_student_toe(student1)
    ouder1.voeg_student_toe(student2)
    ouder1.voeg_student_toe(student3)
    print(ouder1)

    ouder1.geef_info_studenten()
    print(f"De verschillende opleidingen van de kinderen zijn: {ouder1.geef_opleidingen_studenten()}")

    # bespreek onderstaande code mbv de verschillende klasses
    print("\nOuder wordt de eigenaar van een auto.\nDe info van de auto is:")
    auto1 = Auto("1-DVX-656", ouder1)
    print(auto1)

    print("\nOuder geeft auto door aan één van zijn kinderen.\nDe info van de auto is:")
    auto1.eigenaar = student1
    print(auto1)


test_ouder()
