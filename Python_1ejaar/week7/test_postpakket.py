from model.Postpakket import Postpakket

bol = Postpakket("GSM", 3, 3, 4)
print(bol)

print(f"Volume van pakket is: {bol.volume:.2f}")

amazon = Postpakket("Alexa", 3.3, 34, 3)
print(amazon)
