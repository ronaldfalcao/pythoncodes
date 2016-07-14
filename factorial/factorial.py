#coding: utf-8

# The function factorial (not recursive function) return a value for positive numbers, or 1 for input 0 (zero),
# and -1 for negative inputs

def factorial(number):

    factorial = 1

    if number < 0:
        return -1 # The input value not is positive value.
    elif number == 0:
        return 1 # The factorial of zero return 1
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        return factorial # Return a value for input (integer and positive)

#Exemplo de uso da função factorial()
num = int(input("Entre com um número (inteiro e positivo): "))

if (factorial(num) < 0):
    print "O valor de entrada precisa ser um inteiro positivo!"
elif (factorial(num) == 0):
    print "O valor para o fatorial de 0 é 1 por definição."
else:
    print "O valor do fatorial para a posição", num, "é", factorial(num)
