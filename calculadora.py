num1 = (input("Digite um numero: "))
num2 = (input("Digite outro numero: "))



def calculadora(num1, num2, valor):
    if(valor == "Soma"):
        resultado = num1 + num2

    elif(valor == "subtração"):
        resultado = num1 - num2

    elif(valor == "multiplicação"):
        resultado = num1 * num2

    elif(valor == "divisão"):
        resultado = num1/num2
        if num2 != 0:
            resultado = num1/num2

        else:
            resultado = "Erro: Divisão por Zero"

        return resultado


    
    