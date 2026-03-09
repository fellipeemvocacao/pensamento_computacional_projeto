'''

CRUD

Padaria

O sistema da padaria deve permitir o acesso ao menu de produtos e promoções, onde o cliente pode selecionar 
os itens desejados e adiciona-los ao pedido. O sistema deve calcular o valor do pedido de acordo com o valor
do produto selecionado. O sistema deve permitir que o cliente possa finalizar o pedido, e escolher entre a
retirada no estabelecimento ou a entrega. E, então, escolher o método de pagamento, onde o cliente possa escolher entre 
dinheiro, pix, ou cartão de crédito ou débito. O sistema deve confirmar se o pedido chegou ao estabelecimento.

'''

print('Padaria Peter Pão - o melhor pão da cidade!🥞🥐🥖')

nome_gentil = input('Qual é o seu nome?: ')

print(f'Olá, {nome_gentil}! Seja bem-vindo(a) à nossa padaria!')

print("1- Fazer cadastro")
print("2- Ver o cardápio")
print("3- Meus pedidos")
print("4- Informações")
print("0- Sair")


acesso_menu = input("\n O que você quer fazer?: ")

while True:

   if acesso_menu == "1":
       print("Fazer cadastro")


       email_cliente = input("Digite o email:")
       endereço_cliente = input("Digite o endereço:")
       telefone_cliente = input("Digite o telefone:")

       print("Cadastro realizado com sucesso!")
       #Código para fazer cadastro
       break
      
   elif acesso_menu == "2":
       print("Ver o cardápio")
       print("1- Salgados")
       print("2- Doces")
       print("3- Bebidas")
       print("4- Promoções")
       print("5- Lanches")
       opcao_numero = input("Escolha uma opção: ")
       if opcao_numero == "1":
          print("Salgados")
          print("1 - Coxinha - R$5,00")
          print("2 - Kibe - R$6,00")
          print("3 - Empada - R$4,00")
          print("4 - Esfiha - R$5,00")
          print("5 - Pão de queijo - R$3,00")
          print("6 - Pão francês - R$2,00")
          print("7 - Pão na chapa - R$3,50")
          print("8 - Torta de frango - R$8,00")
          break

       elif opcao_numero == "2":
         print("Doces")
         print("9 - Brigadeiro - R$3,00")
         print("10 - Beijinho - R$3,00")
         print("11 - Pudim - R$5,00")
         print("12 - Torta de limão - R$6,00")
         print("13 - Torta de morango - R$7,00")
         print("14 - Torta de chocolate - R$8,00")
         print("15 - Sonho de doce de leite - R$6,00")
         print("16 - Sonho de chocolate - R$7,00")
         print("17 - Bolo de cenoura - R$10,00")
         print("18 - Bolo de chocolate - R$12,00")
         print("19 - Bolo de laranja - R$11,00")
         break
        
       elif opcao_numero == "3":
         print("Bebidas")
         print("20 - Suco de laranja - R$4,00")
         print("21 - Suco de maracujá - R$4,00")
         print("22 - Suco de abacaxi - R$4,00")
         print("23 - Suco de uva - R$4,00")
         print("24 - Suco de limão - R$4,00")
         print("25 - Refrigerante - R$5,00")
         print("26 - Água mineral - R$2,00")
         print("27 - Café - R$3,00")
         print("28 - Chá - R$3,00")
         break

       elif opcao_numero == "4":
         print("Promoções")
         print("29 - Combo 1: Coxinha + Suco de laranja - R$8,00")
         print("30 - Combo 2: Torta de frango + Refrigerante - R$12,00")
         print("31 - Combo 3: Bolo de chocolate + Café - R$14,00")
         print("32 - Combo 4: Pão de queijo + Chá - R$5,00")
         print("33 - Combo 5: Esfiha + Suco de maracujá - R$7,00")
         #Código para exibir promoções
         break
    
       
 

   elif acesso_menu == "3":
        print("Meus pedidos")

        print("Exibir meus pedidos")
        print("1 - A pagar")
        print("2 - Preparando")
        print("3 - A caminho")
        print("4 - Finalizado")
        print("5 - Cancelado")
        print("6 - Reembolso")
        opcao: str = input("Escolha uma opção: ")
        #Código para exibir meus pedidos
        break

   elif acesso_menu == "4":
       print("Informações")
    
       print("Informações")
       print("Endereço: Rua dos Pães, 123 - Centro")
       print("Telefone: (11) 1234-5678")
       print("Horário de funcionamento: Segunda a sábado, das 6h às 20h")
        #Código para exibir informações
       break
   elif acesso_menu == "0":
       print("Sair")    
       #Código para sair
       break
   
   else:
    print("Opção inválida. Por favor, tente novamnete.")