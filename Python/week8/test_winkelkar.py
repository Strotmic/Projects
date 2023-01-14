from model.Winkelkar import Winkelkar

action_kar = Winkelkar()
action_kar.voeg_product_toe("cd1")
action_kar.voeg_product_toe("cd2")
action_kar.voeg_product_toe("cd3")
action_kar.voeg_product_toe("cd4")
action_kar.verwijder_product("cd3")
ikea_kar = Winkelkar()
ikea_kar.voeg_product_toe("Billy")
ikea_kar.voeg_product_toe("Factum")

print(f"Winkelkar 1: {action_kar}")
print(f"Winkelkar 2: {ikea_kar}")


# NIEUW WEEK 08
# print("***** Winkelkar 3 = Winkelkar 1 + Winkelkar 2 *****")
# kerst_kar = action_kar + ikea_kar
# print(f"Winkelkar 3: {kerst_kar}")
# print("***** Winkelkar 1 +=Winkelkar 2 *****")
# action_kar += ikea_kar
# print(f"Winkelkar 1: {action_kar}")
