#Login
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


#Login seguro

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



#Login Invisível


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


#Login com tentativas

import getpass
import hashlib

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def realizar_login_restrito():
    
    usuario_correto = "admin"
    
    hash_correto = "Ivanmaravilhoso"
    
    tentativas_maximas = 3
    tentativas_restantes = tentativas_maximas

    print('\n' + '='*30)
    print('  SISTEMA DE ACESSO RESTRITO  ')
    print('='*30)

    while tentativas_restantes > 0:
        usuario_digitado = input(f'\nUsuário (Tentativas: {tentativas_restantes}): ').strip()
        senha_digitada = getpass.getpass('Senha: ')

       
        if usuario_digitado == usuario_correto and gerar_hash(senha_digitada) == hash_correto:
            print(f'\n[ACESSO CONCEDIDO] Bem-vindo, {usuario_digitado}!')
            return True
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(f'[ERRO] Credenciais incorretas! Você tem mais {tentativas_restantes} tentativa(s).')
            else:
                print('\n[BLOQUEADO] Limite de tentativas excedido. Procure o administrador.')
    
    return False

if __name__ == "__main__":
    realizar_login_restrito()
