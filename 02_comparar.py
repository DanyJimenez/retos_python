#Recibir dos números y determinar cual es mayor

numOne = int(input("Digite un número: "))
numTwo = int(input("Digite otro número: "))

  

        

if  numOne < numTwo:
  print(f"{numOne} es menor que {numTwo}")

elif numOne == numTwo:
  print(f"{numOne} y {numTwo} son iguales. ")
  
else:
  print(f"{numOne} es mayor que {numTwo}")