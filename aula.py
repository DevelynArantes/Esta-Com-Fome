fome = None
usuario = input("Você esta com fome?[S]im ou [N]ão ") 

if usuario == 'Sim':

    fome = True

elif usuario == 'Não':

    fome = False
else:
    print("Ué, eu não entendi a sua resposta")

if fome is True:
    print("Beleza! Então vamos comer!")
if fome is False:
    print("Beleza, sem comida agora!")

