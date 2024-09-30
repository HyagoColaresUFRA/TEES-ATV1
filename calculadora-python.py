import math

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo!"
    return math.factorial(x)

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def exponenciacao(x, y):
    return x ** y

def calculadora():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Fatorial")
    print("6 - Exponenciação")

    escolha = input("Digite o número da operação (1/2/3/4/5/6): ")

    if escolha in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '5':
            print(f"{num1}! = {fatorial(num1)}")
        else:
            num2 = float(input("Digite o segundo número: "))
        if escolha == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
        elif escolha == '6':
            print(f"{num1} ^ {num2} = {exponenciacao(num1, num2)}")
    else:
        print("Operação inválida!")

if __name__ == "__main__":
    calculadora()
