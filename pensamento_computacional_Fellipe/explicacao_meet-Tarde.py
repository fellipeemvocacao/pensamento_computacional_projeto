'''



print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')
operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /')

if operar_numb == '4':
    if int(numb_dois) != 0:
        result = int(numb_hum) / int(numb_dois)
        print(f'O resultado é: {result}')
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operar_numb == '3':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '2':
    result = int(numb_hum) - int(numb_hum)
    print(f'O resultado é: {result}')

elif operar_numb == '1':
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')
    

else:
    print("Número não é válido, tente novamente!")


    

    frutas = ['maçã','banana','laranja','abacaxi']

frutas.append('amora')
frutas.append('mirtilo')
frutas.append('melancia')


print(frutas[5])


print('===GPS - Do Meu Amigo===')

cores = ('preto','magenta','ciano','amarelo','verde')

location_go = (- 23.5505, -46.6333)

location_go_somewhere = (-23.4905, -47.4305)

print(f"Coordenadas de São Paulo: ")



numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')
operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /, 5 -> %')


if operar_numb == '5':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
elif operar_numb == '4':
    if int(numb_dois) != 0:
        result = int(numb_hum) / int(numb_dois)
        print(f'O resultado é: {result}')
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operar_numb == '3':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '2':
    result = int(numb_hum) - int(numb_hum)
    print(f'O resultado é: {result}')

elif operar_numb == '1':
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')
    

else:
    print("Número não é válido, tente novamente!")
    


num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1 > num2:
    print(f" O maior número é o {num1}")
elif num1 < num2:
    print(f" O maior número é o {num2}")
else:
    print("Os dois números são iguais")


idade_pessoa = int(input('Digite sua idade: '))

if idade_pessoa <= 18:
    print('Você é uma criança')

elif idade_pessoa > 18 and idade_pessoa < 20:
    print('Você é um jovem maior de 18 anos')

elif idade_pessoa >= 20 and idade_pessoa < 60:
    print('Você é uma pessoa adulta')

elif idade_pessoa > 60:
    print('Você é uma pessoa idosa')

else:
    print('Digite novamente')



nome_usuario = input('Digite seu nome de usuário: ')
senha_usuario = input('Digite sua senha: ')


print('Login realizado com sucesso')



print('\nTela de login - Meet\n')

nome_usuario = input('Digite seu login para continuar: ')
senha_usuario = input('Digite sua senha para continuar: ')

def realizar_Login():

   senha_padrao:1234 
   print('\nTela de login - Meet\n')

   nome_usuario = input('Digite seu login para continuar: ')
   senha_usuario = input('Digite sua senha para continuar: ')
   print(f' Bem vindo {nome_usuario}!')


 if senha_padrao: 
    print('Senha correta!')
   
   else:
    print('Senha incorreta')
    print(f' Bem vindo, {nome_usuario}!')

    print('---------------------------\n')


realizar_Login()





def realizar_login_seguro():
    senha_padrao = "1234"

    print('\n--- Sistema de Login Seguro ---')
    nome_usuario = input('Digite seu login: ')
    senha_digitada = input('Digite sua senha: ')

    if senha_digitada == senha_padrao:
        print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}! Acesso concedido.')
    else:
        print('\n[ERRO] Senha incorreta! Acesso negado.')

        print('---------------------------\n')

realizar_login_seguro()



import getpass


def realizar_login_invisivel():

    senha_padrao = "1234"

    print('\n--- Sistema de Login Protegido ---')
    nome_usuario = input('Digite seu login: ')

    senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão):')

    if senha_digitada == senha_padrao:
        print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
    else:
        print('\n[ERRO] Senha incorreta!')

    print('----------------------------------\n')

realizar_login_invisivel


numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')
operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /, 5 -> %')


if operar_numb == '5':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
elif operar_numb == '4':
    if int(numb_dois) != 0:
        result = int(numb_hum) / int(numb_dois)
        print(f'O resultado é: {result}')
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operar_numb == '3':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '2':
    result = int(numb_hum) - int(numb_hum)
    print(f'O resultado é: {result}')

elif operar_numb == '1':
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')
    

else:
    print("Número não é válido, tente novamente!")
    


num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1 > num2:
    print(f" O maior número é o {num1}")
elif num1 < num2:
    print(f" O maior número é o {num2}")
else:
    print("Os dois números são iguais")


idade_pessoa = int(input('Digite sua idade: '))

if idade_pessoa <= 18:
    print('Você é uma criança')

elif idade_pessoa > 18 and idade_pessoa < 20:
    print('Você é um jovem maior de 18 anos')

elif idade_pessoa >= 20 and idade_pessoa < 60:
    print('Você é uma pessoa adulta')

elif idade_pessoa > 60:
    print('Você é uma pessoa idosa')

else:
    print('Digite novamente')



    

frutas = ['maçã','banana','laranja','abacaxi']

frutas.append('amora')
frutas.append('mirtilo')
frutas.append('melancia')


print(frutas[5])


print('===GPS - Do Meu Amigo===')

cores = ('preto','magenta','ciano','amarelo','verde')

location_go = (- 23.5505, -46.6333)

location_go_somewhere = (-23.4905, -47.4305)

print(f"Coordenadas de São Paulo: ")

nome_aluno = input("Digite seu nome: ")
print(f"Olá, {nome_aluno}!")

nota1_aluno = float(input("Digite sua nota do 1° Bimestre: "))
nota2_aluno = float(input("Digite sua nota do 2° Bimestre: "))
nota3_aluno = float(input("Digite sua nota do 3° Bimestre: "))
nota4_aluno = float(input("Digite sua nota do 4° Bimestre: "))

def calcula_media(nota1, nota2, nota3, nota4):
  media = (nota1 + nota2 + nota3 + nota4) / 4
  if media >= 7:
   return media, "Aprovado"
  else:
   return media, "Reprovado"
  
resultado, status = calcula_media(nota1_aluno, nota2_aluno, nota3_aluno, nota4_aluno)
print("=" * 30)
print(f"Aluno: {nome_aluno}")
print(f"Média Final: {resultado:.1f}") 
print(f"Status: {status}")
print("=" * 30)


def ler_arquivo_jovens():
    print('Sistema de upload dos arquivos jovens')
    print('-' * 30)

    with open('arquivo_lido.txt', 'r', encoding= 'utf-8') as arquivo:
        conteudo = arquivo.read() 
        print(conteudo)  

ler_arquivo_jovens()

def sobrescrever_arquivo():
    print('--- Sistema de upload dos arquivos jovens (Modo Sobrescrever) ---')
    

    conteudo_novo = input("\nDigite o que deseja salvar (ISSO APAGARÁ O QUE ESTAVA LÁ): ")

    
    with open('arquivo_lido.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_novo + "\n")
    
    print("\n[AVISO] O arquivo foi limpo e o novo conteúdo foi gravado!")

def ler_arquivo_jovens():
    print('\n--- Lendo o arquivo agora ---')
    try:
        with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo ainda não existe.")


sobrescrever_arquivo()
ler_arquivo_jovens()

'''




