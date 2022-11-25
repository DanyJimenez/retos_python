#Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?


juan = int(input("¿Cuánto dinero tenés en el bolsillo, Juan? $"))

camila = round(juan/2,3)

ricardo = round((camila + juan) / 2,3)

print(f"Juan tiene ${juan} en su bolsillo, Camila tiene ${camila} y Ricardo ${ricardo} ")
