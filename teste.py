from Ativ3 import Lista

lista = Lista(5)

print("=== TESTE ADICIONAR ===")
print(lista.adicionar(10))
print(lista.adicionar(20))
print(lista.adicionar(30))
print(lista.adicionar(40))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE PESQUISAR ===")
print("Posição do 20:", lista.pesquisar(20))
print("Posição do 99:", lista.pesquisar(99))

print("\n=== TESTE OBTER ===")
print("Posição 0:", lista.obter(0))
print("Posição 2:", lista.obter(2))
print("Posição 10:", lista.obter(10))

print("\n=== TESTE INSERIR ===")
print("Inserindo 15 na posição 1:", lista.inserir(1, 15))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)
print("Inserindo 5 na posição 0:", lista.inserir(0, 5))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE REMOVER ===")
print("Removendo posição 2:", lista.remover(2))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)
print("Removendo posição 0:", lista.remover(0))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== TESTE REMOVER_NUMERO ===")
print("Removendo o número 30:", lista.remover_numero(30))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)
print("Tentando remover o número 99:", lista.remover_numero(99))
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)

print("\n=== ESTADO FINAL ===")
print("Array:", lista.array)
print("Tamanho:", lista.tamanho)