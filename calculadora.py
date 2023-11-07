
def calculadora():
    
    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
    
        escreva = input("Digite o comando da operação desejada:")

        if(escreva == 0):
            print("Sair da calculadora")
            break
        elif escreva in ('1','2','3','4'):
            num1 = float(input("Qual irá ser o primeiro numero: "))
            num2 = float(input("Qual irá ser seu segundo numero "))

            if(escreva == '1'):
                    resultado = num1 +num2        
                    print(f"Resultado: {num1} + {num2} = {resultado}")

            elif(escreva == '2'):
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
        
            elif(escreva == '3'):
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
        
            

            elif(escreva == "4"):
                if(num2 != 0):
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
            
                else:
                    print("Erro em sua divisão")
            else:
                print(". escolha uma operação valida" )
        else:
            print("Essa opção não existe. escolha uma opção valida fazendo favor")

    
if __name__ == "__main__":
    calculadora() 



    
    