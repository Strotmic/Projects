from model.Presentator import Presentator


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")
presentator3 = Presentator("Laura", "Omloop")
presentator_copy = Presentator("Laura", "Tesoro")

print("***test print***")
print(presentator1)
print("\n***test vergelijking***")
if presentator1 == presentator2:
    print(f"{presentator1} is gelijk aan {presentator2}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator2}")

if presentator1 == presentator3:
    print(f"{presentator1} is gelijk aan {presentator3}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator3}")


if presentator1 == presentator_copy:
    print(f"{presentator1} is gelijk aan {presentator_copy}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator_copy}")
