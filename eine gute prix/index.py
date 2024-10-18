import random

# eine just prix

object_list =["Agenda","Allumette","Arrosoir","Aspirateur","Aspirateur connecté","Assiette","Balance","Barrette","Bougie","Bouteille","Briquet","Brosse à dents","Cafetière","Cahier","Caméra","Carnet","Chaise","Cloche","Colle"]
number = random.randint(0,1000)
object_number = random.randint(0, 17)
i = 0
while i = object_number:
    object_list[i]
    i++

print("bienvenue au juste prix bande neuille frère")
print("aujourd'hui vous devez devinez le prix de " + object)

while True:
    player_number = input("Essèye de deviné le nombre sale tête de neuille frère :")
    player_number = int(player_number)
    if player_number < number:
        print("trop petit frère")
    elif player_number > number:
        print("trop grand frère")
    else:
        print("tu as trouvé GG frère")
        break

