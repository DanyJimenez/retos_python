#Recibir un numero en teclado y determinar si este es múltiplo de 3

randomNumber = int(input("Digite un número: "))

if randomNumber % 3 == 0:
  print(f"{randomNumber} es múltiplo de 3")
else:
  print(f"{randomNumber} no es múltiplo de 3")