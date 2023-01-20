
from model.Meetwiel import Meetwiel

meetwiel1 = Meetwiel(0.9)  # straal
meetwiel2 = Meetwiel(0.45, 123)  # straal , omwentelingen
print(meetwiel1)
print(meetwiel2)

waarde = input(
    "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
while (waarde != "c" and waarde.isnumeric()):
    meetwiel1.omwentelingen += int(waarde)
    waarde = input(
        "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
print(meetwiel1)
print(f"Meetwiel 1 legde reeds {meetwiel1.afgelegde_afstand:.2f} m af")
