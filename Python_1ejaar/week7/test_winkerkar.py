from model.Winkelkar import Winkelkar

action_kar = Winkelkar()
action_kar.voeg_product_toe("cd1")
action_kar.voeg_product_toe("cd2")
action_kar.voeg_product_toe("cd3")
action_kar.voeg_product_toe("cd4")
# action_kar.verwijder_product("cd5")

ikea_kar = Winkelkar()
ikea_kar.voeg_product_toe("Billy")
ikea_kar.voeg_product_toe("Factum")

print(f"Winkelkar 1: {action_kar}\n")
print(f"Winkelkar 2: {ikea_kar}\n")

ikea_kar.verwijder_product('Billy')
print(f"Winkelkar 2: {ikea_kar}\n")

