from lista_ligada import ListaLigada
class Pilha:
  def __init__(self):
    self._elemento = Listaligada()

  def getElemento(self):
    return self._elemento
  def setElemento(self, elemento):
    self._elemento = elemento

  def push(self, item): #Empilhar
    self._elemento.inserir_inicio(item)

  def pop(self): #Desempilhar
    if self.is_empty():
      return None #Evita Underflow
    return self._elemento.remover_inicio()

  def peek(self):#Olhar o topo da lista
    if self.is_empty():
      return None
    return self._elementos.primeiro.item

  def is_empty(self):#Validação
    return self._elementos.vazia()

#Algoritmo de conversão
def decimal_para_binario(numero):
  pilha = instanciar_nova_pilha()

  if numero > 0:
    resto = numero % 2
    pilha.push(resto) #Fase 1: Empilhar restos
    numero = numero / 2

  binario = ""

  if not pilha.is_empty():
    #Fase2: Desempilhar na ordem correta LIFO
    binario += string(pilha.pop())
  
  return binario
