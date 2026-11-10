from pilha import Pilha

#Algoritmo de conversão
def decimal_para_binario(numero):
  pilha = Pilha()

  while numero > 0:
    resto = numero % 2
    pilha.push(resto) #Fase 1: Empilhar restos
    numero = numero / 2

  binario = ""

  while not pilha.vazia():
    #Fase2: Desempilhar na ordem correta LIFO
    binario += string(pilha.pop())
  
  return binario
