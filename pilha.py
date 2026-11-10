from lista_ligada import ListaLigada
class Pilha:
  def __init__(self):
    self._elementos = Listaligada()

  def push(self, item): #Empilhar
    self._elementos.inserir_inicio(item)

  def pop(self): #Desempilhar
    return self._elementos.remover_inicio()

  def vazia(self):#Validação
    return self._elementos.vazia()

  def peek(self):#Olhar o topo da lista
    if self.vazia():
      return None
    return self._elementos.primeiro.item

  def tamanho(self):
    return self._elementos.tamanho
  
