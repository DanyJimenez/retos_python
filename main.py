# Recibir un numero en teclado y determinar si este es múltiplo de 5

randomNumber = int(input("Digite un número: "))

if randomNumber % 5 == 0:
  print(f"{randomNumber} es múltiplo de 5")
else:
  print(f"{randomNumber} no es múltiplo de 5")