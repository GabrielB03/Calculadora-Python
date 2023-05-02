def bem_vindo():
    print('''
Bem vindo a calculadora
    ''')

def calcular():

    operacao = input('''
Por favor, escreva a operação que você gostaria de usar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
** para expoente
% para módulo
''')

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Adição
    if (operacao == '+'):
        print("{} + {} = ".format(numero1, numero2))
        print(numero1 + numero2)

    # Subtração
    elif (operacao == '-'):
        print("{} - {} = ".format(numero1, numero2))
        print(numero1 - numero2)

    #Multiplicação
    elif (operacao == '*'):
        print("{} * {} = ".format(numero1, numero2))
        print(numero1 * numero2)

    # Divisão
    elif (operacao == '/'):
        print("{} / {} = ".format(numero1, numero2))
        print(numero1 / numero2)

    # Expoente
    elif (operacao == '**'):
        print("{} ** {} = ".format(numero1, numero2))
        print(numero1 ** numero2)

    # Módulo
    elif (operacao == '%'):
        print("{} % {} = ".format(numero1, numero2))
        print(numero1 % numero2)

    else:
        print("Você não digitou um operador válido, por favor rode o programa de novo.")

    #Adicionar a função repetir() para a função calcular()
    repetir()

def repetir():

    #Pega a entrada do usuário
    calcular_denovo = input('''
Você quer calcular de novo?
Por favor digite S para sim ou N para não.
    ''')

    #Se o o usuário digitar S, rode a função calcular() e aceitar 'y' ou 'Y' adicionando str.upper()
    if calcular_denovo.upper() == 'S':
        calcular()

    #Se o usuário digitar N, diga tchau para o usuário no final do programa e aceitar 'n' ou 'N' adicionando str.upper()
    elif calcular_denovo.upper() == 'N':
        print("Vejo você depois.")

    #Se o usuário digitar outra coisa que não seja S ou N, repetir o programa
    else:
        repetir()

bem_vindo()

#Chamar calcular() fora da função
calcular()