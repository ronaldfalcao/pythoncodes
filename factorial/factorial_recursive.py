#coding: utf-8


def factorial_recursive(x):
    if x == 0:
        return 1
    elif x == 1: # Base case
        return 1
    else:
        return x * factorial_recursive(x-1) # Recursive expression

#Exemplo de uso da função factorial()
num = int(input("Entre com um número (inteiro e positivo): "))

if (factorial_recursive(num) < 0):
    print "O valor de entrada precisa ser um inteiro positivo!"
elif (factorial_recursive(num) == 0):
    print "O valor para o fatorial de 0 é 1 por definição."
else:
    print "O valor do fatorial para a posição", num, "é", factorial_recursive(num)
