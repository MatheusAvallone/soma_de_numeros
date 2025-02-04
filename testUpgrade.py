import operacoes

Stop=True
while Stop:

    numero1input=int(input("digite um numero "))
    numero2input=int(input("digite outro numero "))


    operadorInput=input("tipo de operador ")
    match operadorInput:
        case "+":
            print(operacoes.somarNumero(numero1input,numero2input))
        case "-":
            print(operacoes.subtrairNumero(numero1input,numero2input))
        case "*":
            print(operacoes.multiplicacaoNumero(numero1input,numero2input))
        case "/":
            print(operacoes.dividirNumero(numero1input,numero2input))


        case _:
            Stop=False
            print("Operador Invalido")
