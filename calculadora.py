print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')
operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /: ')

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
    print("Número não é válido, tente novamnete!")

historico = []

while True:
    print("\n--- Calculadora média - Python ---")
    print("1. Operações Básicas (+, -, *, /)")
    print("2. Calcular Porcentagem (X% de Y)")
    print("3. Ver Histórico")
    print("0. Sair")
    
    opcao = input("Escolha: ")

    if opcao == '1':
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        op = input("Operação (+, -, *, /): ")
        
        if op == '+': res = n1 + n2
        elif op == '-': res = n1 - n2
        elif op == '*': res = n1 * n2
        elif op == '/': res = n1 / n2 if n2 != 0 else "Erro"
        
        calc = f"{n1} {op} {n2} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '2':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '3':
        print("\n-- Histórico --")
        for item in historico:
            print(item)
            
    elif opcao == '0': break

    historico_detalhado = []

while True:
    print("\n==============================")
    print("    \nCalculadora - Python")
    print("==============================")
    print("1. Calcular (Inteiro/Decimal)")
    print("2. Porcentagem")
    print("3. Ver Histórico Detalhado")
    print("0. Sair")
    
    escolha = input("\nOpção: ")

    if escolha == '1':
        # Entrada de dados
        v1 = input("Primeiro número: ")
        v2 = input("Segundo número: ")
        
        # Lógica para converter (verifica se há ponto para ser float ou int)
        n1 = float(v1) if '.' in v1 else int(v1)
        n2 = float(v2) if '.' in v2 else int(v2)
        
        print("Operações: [1]+ [2]- [3]* [4]/")
        op_mat = input("Operação: ")
        
        if op_mat == '1': simbola, res = "+", n1 + n2
        elif op_mat == '2': simbola, res = "-", n1 - n2
        elif op_mat == '3': simbola, res = "*", n1 * n2
        elif op_mat == '4': 
            simbola = "/"
            res = n1 / n2 if n2 != 0 else "Indeterminado"
        
        registro = f"Cálculo: {n1} {simbola} {n2} | Resultado: {res} | Tipo: {type(res).__name__}"
        print(f"\n>> {registro}")
        historico_detalhado.append(registro)

    elif escolha == '2':
        # Ex: 10% de aumento em 100 reais
        v_porcent = float(input("Valor da porcentagem: "))
        v_total = float(input("Valor base: "))
        
        print("1. Calcular apenas a parte (X% de Y)")
        print("2. Acréscimo (Y + X%)")
        print("3. Desconto (Y - X%)")
        tipo_p = input("Opção: ")
        
        parte = (v_porcent / 100) * v_total
        
        if tipo_p == '1':
            res_p = parte
            msg = f"{v_porcent}% de {v_total} é {res_p}"
        elif tipo_p == '2':
            res_p = v_total + parte
            msg = f"{v_total} com acréscimo de {v_porcent}% = {res_p}"
        elif tipo_p == '3':
            res_p = v_total - parte
            msg = f"{v_total} com desconto de {v_porcent}% = {res_p}"
            
        print(f"\n>> {msg}")
        historico_detalhado.append(msg)

    elif escolha == '3':
        print("\n--- HISTÓRICO DE OPERAÇÕES ---")
        if not historico_detalhado:
            print("Nenhum cálculo realizado.")
        else:
            for i, item in enumerate(historico_detalhado, 1):
                print(f"{i}. {item}")

    elif escolha == '0':
        print("Encerrando... Até à próxima!")