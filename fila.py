from lista_ligada import ListaLigada
class Fila:
  def __init__(self):
    self._elementos = ListaLigada()

  def enqueue(self, item):
    self._elementos.adicionar(item)

  def dequeue(self):
    return self._elementos.remover_inicio()

  def peek(self):
    if self.vazia():
      return None
    return self._elementos.primeiro.item

  def vazia(self):
    return self._elementos.vazia()

  def size(self):
    return self._elementos.tamanho
