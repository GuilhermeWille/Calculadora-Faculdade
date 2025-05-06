saida = ''

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não foi possivel dividir por zero(0)"
    return x / y

def calculadora(num1, num2, operacao):
    operacao.lower()
   
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida!'
    
    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou nome): ")

        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Entrada inválida! Tente novamente.")

    saida = input("Deseja realizar outra opera operação? (S/N): ")
    
    if saida == 'n':
        print("Volte sempre :)")
