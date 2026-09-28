from Ativ3 import Lista

lista = Lista(5)

print("=== TESTE ADICIONAR ===")
print(lista.adicionar(7))
print(lista.adicionar(17))
print(lista.adicionar(77))
print(lista.adicionar(37))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE PESQUISAR ===")
print("Posição do 7:", lista.pesquisar(7))
print("Posição do 99:", lista.pesquisar(99))

print("\n=== TESTE OBTER ===")
print("Posição 0:", lista.obter(0))
print("Posição 2:", lista.obter(2))
print("Posição 10:", lista.obter(10))

print("\n=== TESTE INSERIR ===")
print("Inserindo 27 na posição 2:", lista.inserir(2, 27))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE REMOVER ===")
print("Removendo posição 2:", lista.remover(2))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE REMOVER_NUMERO ===")
print("Removendo o número 77:", lista.remover_numero(77))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)
