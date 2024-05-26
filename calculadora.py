"""" Calculadora """

#variables para pedir los numero que deseara ingresar el usuario
n1 = int(input("Eliga su primer numero: "))
n2 = int(input("Eliga su segundo numero: "))

#Se le pide al usuario que eliga el tipo de operacion
operacion = input("Introduzca la operacion que desea realizar (+, -, * o /): ")

# se crea la logica de las operaciones que se desen realizar
match operacion:
    case "+":
        res = n1 + n2
    case "-":
        res = n1 - n2
    case "*":
        res = n1 * n2
    case "/":
        res = n1 / n2

#Se imprime el resultado
print(f"El resultado de su operacion {n1} {operacion} {n2} = {res}")
