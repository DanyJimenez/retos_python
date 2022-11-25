#Una compañía de software contable, paga a su personal de ventas un salario de 3500000 mensuales, mas una comisión de 1500000 por cada licencia de software vendida menos el (5% del salario total + comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario mensual de un vendedor dado recibiendo el numero de ventas realizadas

nombre = input("Digite su nombre: ")
identificacion = input("Digite su identificación: ")
numComision = int(input(f"¿Cuantas licencias de software vendió este mes, {nombre}? "))

salario = 3500000
valorcomision = 1500000 

totalComision = valorcomision*numComision
deducciones = salario * 5 /100
salario_menos_deducciones = salario - deducciones
salarioTotal = salario_menos_deducciones + totalComision

#aplicativo
print("--"*30)
print("COMPUVENTA S.A")
print("Nombre del empleado: ", nombre)
print("Número de identificación: ", identificacion)
print(f"Su salario (${3500000}) - deducciones (5%) + comisiones de venta x {numComision} (${totalComision}) es: $", salarioTotal)