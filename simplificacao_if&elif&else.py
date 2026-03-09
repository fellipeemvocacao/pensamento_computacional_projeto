preco_frutas = {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0
}

# Definimos qual fruta queremos procurar
fruta_desejada = 'laranja'

# Fazemos a busca direta usando o método .get()
# O .get() tenta encontrar a fruta; se não achar, mostra 'Fruta não encontrada'
resultado = preco_frutas.get(fruta_desejada, 'Fruta não encontrada')

# Exibindo o resultado
print(f"O preço da {fruta_desejada} é R${resultado}")
