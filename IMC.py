# Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. Sabendo que a fórmula para calcular
# o IMC é: peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.

def massa_corporal(peso,altura):
    imc = peso/(altura*altura)*10000

    if (imc <= 18.5 ): return "Magreza"

    elif(imc >18.5) and (imc <= 24.9): return "Peso adequado"

    elif(imc >= 25) and (imc <= 29.9): return "Sobrepeso"

    elif(imc > 30.0) and (imc <= 34.9): return "Obesidade Grau1"

    elif (imc > 35.0) and (imc <= 40.0): return "Obesidade grau 2"


    peso = 80
    altura = 177

    resultado = massa_corporal(peso,altura)
    print(resultado) 



