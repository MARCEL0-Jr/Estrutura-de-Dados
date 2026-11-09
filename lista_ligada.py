from no import No

class Lista_Ligada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0

    def adicionar(self, item):
        """ Adiciona no fim da lista """

        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def __str__(self):
        """ Retorna os itens da lista como uma string. """

        no_atual = self.primeiro
        texto = ""
        while no_atual:
            texto += str(no_atual.item) + " -> "
            no_atual = no_atual.proximo
        return texto + "null"
    
    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. """

        atual = self.primeiro

        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo
        
        return False

        #Custo O(n), no pior caso percorre todos os nós da lista. 

    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. """

        if posicaso < 0 or posicao >= self.tamanho:
            return None
        
        atual = self.primeiro

        for i in range(posicao):
            atual = atual.proximo
        
        return atual.item 

        #Custo O(n), precisa percorrer os nós até achar a posição do item desejado. No melhor caso, se a posição for zero, é O(1).

    def inserir(self, posicao, item):
         """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. """
         
        if posicao < 0 or posicao > self.tamanho:
            return False

        if posicao == 0:
             self.inserir_inicio(item)
             return True

        novo_no = No(item)
        atual = atual.proximo

        for i in range(posicao - 1):
            atual = atual.proximo
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

        self.tamanho += 1

        return True

        #Custo O(n), pode precisar percorrer a lista até achar a posição, no melhor caso é O(1).

    def remover_inicio(self, posicao):
        """ Remove o primeiro item da lista e o retorna """

        if self.primeiro is None:
            return None

        item = self.primeiro.item
        self.primeiro = self.primeiro.proximo
        self.tamanho -= 1

        return item

        #Custo O(1), apenas altera o primeiro nó.

    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. """

        if posicao < 0 or posicao >= self.tamanho:
            return False

        if posicao == 0:
            self.remover_inicio()
            return True

        atual = self.primeiro

        for i in range(posicao - 1):
            atual = atual.proximo

        atual.proximo = atual.proximo.proximo

        self.tamanho -= 1

        return True

        #Custo O(n), precisa percorrer a lista para encontrar o nó anterior.

    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. """

        if self.primeiro is None:
            return False

        if self.primeiro.item == item:
            self.remover_inicio()
            return True

        atual = self.primeiro

        while atual.proximo:
            if atual.proximo.item == item:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True

            atual = atual.proximo

        return False

        #Custo O(n), percorre a lista até encontrar o item.
