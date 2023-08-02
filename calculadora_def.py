# Calculadora utilizando definição de funções

def soma(a, b):
    op = a + b
    print("O resultado da soma é: ", op)

def sub(a, b):
    op = a - b
    print("O resultado da subtração é: ", op)

def mult(a, b):
    op = a * b
    print("O resultado da multiplicação é: ", op)

def div(a, b):
    op = a / b
    print("O resultado da divisão é: ", op)

def list():
    vantagens = ['Qualidades do Python:', '1) Fácil de aprender', '2) Alta empregabilidade', '3) Muito material gratuito']
    for i in vantagens:
        print(i)

print("--- MENU ---")
print("1) Soma")
print("2) Subtração")
print("3) Multiplicação")
print("4) Divisão")
print("5) Listar qualidades do Python")

opcao = input("Selecione a opção desejada: ")

if opcao == "1":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    soma(x, y)

elif opcao == "2":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    sub(x, y)

elif opcao == "3":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    mult(x, y)

elif opcao == "4":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    div(x, y)

elif opcao == "5":
    list()

else:
    print("Opção inválida.")


