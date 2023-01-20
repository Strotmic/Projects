# from model.Hotel import Hotel
# from model.Hotelgast import Hotelgast

# hotel_howest = Hotel("Howest")
# print(hotel_howest)

# hotel_howest.check_in("Walcarius", "Stijn")
# hotel_howest.check_in("Laprudence", "Christophe")

# hotel_howest.bestel_drank("Walcarius", "Stijn", 100)

# print("\n")
# hotel_howest.print_info_gasten()
# print("Stijn betaalt zijn schuld")
# hotel_howest.vereffen_saldo_gast("Walcarius", "Stijn")
# print("******************")
# hotel_howest.check_out("Walcarius", "Stijn")
# print("******************")
# print("\n")
# hotel_howest.print_info_gasten()

# from model.Hotel import Hotel
# from model.Hotelgast import Hotelgast
# hotel_howest = Hotel("Howest") 
# print(hotel_howest)
# hotel_howest.check_in("Walcarius","Stijn") 
# hotel_howest.check_in("Laprudence","Christophe") 
# print("\n")
# hotel_howest.print_info_gasten()
# from model.Hotel import Hotel
# from model.Hotelgast import Hotelgast
# hotel_howest = Hotel("Howest") 
# print(hotel_howest)
# hotel_howest.check_in("Walcarius","Stijn")
# hotel_howest.check_in("Laprudence","Christophe") 
# print("\n")
# hotel_howest.print_info_gasten() 
# print("\n")
# print("******************") 
# hotel_howest.check_out("Walcarius","Stijn") 
# hotel_howest.check_out("Roobrouck","Dieter")
# print("******************")
# print("\n") 
# hotel_howest.print_info_gasten()


# from model.Hotel import Hotel
# from model.Hotelgast import Hotelgast
# hotel_howest = Hotel("Howest")
# print(hotel_howest) 
# hotel_howest.check_in("Walcarius","Stijn")
# hotel_howest.check_in("Laprudence","Christophe")
# hotel_howest.bestel_drank("Walcarius","Stijn",100) 
# print("\n")
# hotel_howest.print_info_gasten()
# print("\n")
# print("******************") 
# hotel_howest.check_out("Walcarius","Stijn") 
# print("******************")
# print("\n")
# hotel_howest.print_info_gasten()

from model.Hotel import Hotel
from model.Hotelgast import Hotelgast
hotel_howest = Hotel("Howest") 
print(hotel_howest)
hotel_howest.check_in("Walcarius","Stijn")
hotel_howest.check_in("Laprudence","Christophe") 
hotel_howest.bestel_drank("Walcarius","Stijn",100)
print("\n")
hotel_howest.print_info_gasten()
print("Stijn betaalt zijn schuld")
hotel_howest.vereffen_saldo_gast("Walcarius", "Stijn")
print("\n")
print("******************")
hotel_howest.check_out("Walcarius","Stijn") 
print("******************")
print("\n")
hotel_howest.print_info_gasten()

print(type(hotel_howest))
