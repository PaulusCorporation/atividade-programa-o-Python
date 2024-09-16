1
def funcao_processamento():
    #Valores aleatorios
    X=  10
    Y=  15
    #Soma da quantidade de passos 
    qtd_passos= X + Y
    #Apresentação do resultado 
    print(f'A quantidade de passos para o pirata será de {qtd_passos}')

if __name__ == '__main__':
    
    #Mensagem de início do programa
    print("--- --- iniciando o programa --- ---")

    #Processamento realizado pelo programa
    funcao_processamento()

    #Mensagem de fim do programa
    print("--- fim do programa --- ---")

2
def funcao_processamento():
    qtd_ferro = float(input('Digite a quantidade de ferro:' ))
    qtd_ouro = float(input('Digite a quantidade de ouro:' ))

    total_liga_metalica = qtd_ferro + qtd_ouro

    if (qtd_ferro/total_liga_metalica) >= 0.7:
        print('Armadura foda mermão!!')
    else:
        print('Agora deu o caraio mermo hein?')

if __name__ == '__main__':

    #Mensagem de início do programa
    print("--- --- iniciando o programa --- ---")

    #Processamento realizado pelo programa
    funcao_processamento()

    #Mensagem de fim do programa
    print("--- fim do programa --- ---")

3
def funcao_processamento():
    print('Digite o seu tipo de animal favorito: ')
    print('1 - Mamífero \n2- Réptil')
    opcao = int(input('Qual sua opção: '))

    if opcao ==1:
        print('Tenho certeza que é uma milf cow')
    else:
        print('Jabuti só pode')
        
if __name__ == '__main__':

#Mensagem de início do programa
    print("--- --- iniciando o programa --- ---")

    #Processamento realizado pelo programa
    funcao_processamento()

    #Mensagem de fim do programa
    print("--- fim do programa --- ---")

4
# Entrada de dados: quantidade de moedas de cada tipo
moedas_1_real = int(input("Digite a quantidade de moedas de 1 real: "))
moedas_50_centavos = int(input("Digite a quantidade de moedas de 50 centavos: "))
moedas_25_centavos = int(input("Digite a quantidade de moedas de 25 centavos: "))

# Cálculo do valor total
total = (moedas_1_real * 1.00) + (moedas_50_centavos * 0.50) + (moedas_25_centavos * 0.25)

# Saída: valor total
print(f"O valor total em reais é: R$ {total:.2f}")

5
# Entrada de dados: quantidade de água disponível (em litros) e a distância até o oásis (em km)
agua_disponivel = float(input("Digite a quantidade de água disponível (em litros): "))
distancia_oasis = float(input("Digite a distância até o oásis (em quilômetros): "))

# Cálculo: quantidade de água necessária
agua_necessaria = distancia_oasis * 2  # 2 litros por quilômetro

# Verificação se a água é suficiente
if agua_disponivel >= agua_necessaria:
    print("A quantidade de água é suficiente para chegar ao oásis.")
else:
    print("A quantidade de água não é suficiente para chegar ao oásis.")

6
# Entrada de dados: distância e tempo do primeiro dragão
distancia_dragao1 = float(input("Digite a distância percorrida pelo primeiro dragão (em km): "))
tempo_dragao1 = float(input("Digite o tempo gasto pelo primeiro dragão (em horas): "))

# Entrada de dados: distância e tempo do segundo dragão
distancia_dragao2= float(input("Digite a distância percorrida pelo segundo dragão (em km): "))
tempo_dragao2 = float(input("Digite o tempo gasto pelo segundo dragão (em horas): "))

# Calculo da velocidade de cada dragão (velocidade = distância/ tempo)
velocidade_dragao1= distancia_dragao1 / tempo_dragao1
velocidade_dragao2= distancia_dragao2 / tempo_dragao2

# Comparação das velocidades e dterminação do dragão mais rápido:
if velocidade_dragao1 > velocidade_dragao2:
    print("O primeiro dragão é mais rápido. ")
elif velocidade_dragao2 > velocidade_dragao1:
    print("O segundo dragão consegue ser mais rápido. ")
else:
    print("Ambos possuem a mesma velocidade")

7
# Entrada de dados: altura da planta
altura_planta = float(input("Digite a altura da planta (em metros): "))

# Classificação da planta com base na altura
if altura_planta < 1:
    print("A planta é pequena.")
elif 1 <= altura_planta <= 3:
    print("A planta é média.")
else:
    print("A planta é grande.")

8
# Entrada de dados: número de missões completadas
missoes_completadas = int(input("Digite o número de missões completadas pelo cavaleiro: "))

# Cálculo do bônus com base nas missões completadas
if missoes_completadas > 10:
    bonus = 100
elif 5 <= missoes_completadas <= 10:
    bonus = 50
else:
    bonus = 10

# Saída: valor do bônus
print(f"O cavaleiro receberá {bonus} moedas de ouro de bônus.")

9
# Entrada de dados: escolha do feitiço
escolha = int(input("Escolha um feitiço (1 para Fogo, 2 para Água, 3 para Terra): "))

# Uso do comando match-case para exibir o feitiço escolhido
match escolha:
    case 1:
        print("Você escolheu o feitiço de Fogo!")
    case 2:
        print("Você escolheu o feitiço de Água!")
    case 3:
        print("Você escolheu o feitiço de Terra!")
    case _:
        print("Escolha inválida.")

10
# Entrada de dados: escolha da porta
porta_escolhida = int(input("Escolha uma porta (1 a 5): "))

# Uso do comando match-case para mostrar o desafio correspondente
match porta_escolhida:
    case 1:
        print("Você enfrentará o Desafio da Chama Eterna!")
    case 2:
        print("Você enfrentará o Desafio da Tempestade Incontrolável!")
    case 3:
        print("Você enfrentará o Desafio do Guardião de Pedra!")
    case 4:
        print("Você enfrentará o Desafio do Labirinto das Sombras!")
    case 5:
        print("Você enfrentará o Desafio do Dragão Ancestral!")
    case _:
        print("Porta inválida. Escolha um número entre 1 e 5.")



