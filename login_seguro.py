import getpass  

def realizar_login_invisivel():
    
    senha_padrao = "1234"

    print('\n--- Sistema de Login Protegido ---')
    nome_usuario = input('Digite seu login: ')


    senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

    if senha_digitada == senha_padrao:
        print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
    else:
        print('\n[ERRO] Senha incorreta!')

    print('----------------------------------\n')

if __name__ == "__main__":
    realizar_login_invisivel()
