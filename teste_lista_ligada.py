import pytest
from lista_ligada import Lista_Ligada

@pytest.fixture
def lista():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    lista.adicionar(40)
    return lista
    
def test_exibir_lista(lista):
    lista.exibir()
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"

def test_inserir_inicio(lista):
    lista.inserir_inicio(7)
    assert lista.primeiro.item == 7
    assert str(lista) == "7 -> 10 -> 20 -> 30 -> 40 -> null"

def test_inserir_inicio_vazia():
    lista0 = ListaLigada()
    lista0.inserir_inicio(7)
    assert lista0.primeiro.item == 7
    assert str(lista0) == "7 -> null"

def test_adicionar(lista):
    lista.adicionar(50)

    assert str(lista) == "10 -> 20 -> 30 -> 40 -> 50 -> null"
    assert lista.tamanho == 5

def test_pesquisar(lista):
    assert lista.pesquisar(20) == True
    assert lista.pesquisar(40) == True
    assert lista.pesquisar(50) == False

def test_obter(lista):
    assert lista.obter(0) == 10
    assert lista.obter(1) == 20
    assert lista.obter(2) == 30
    assert lista.obter(3) == 40
    assert lista.obter(4) == None
    assert lista.obter(-1) == None

def test_inserir(lista):
    assert lista.inserir(2, 25) == True
    assert str(lista) == "10 -> 20 -> 25 -> 30 -> 40 -> null"

    assert lista.inserir(0, 5) == True
    assert str(lista) == "5 -> 10 -> 20 -> 25 -> 30 -> 40 -> null"

    assert lista.inserir(20, 60) == False

def test_remover_inicio(lista):
    item = lista.remover_inicio()

    assert item == 10
    assert str(lista) == "20 -> 30 -> 40 -> null"
    assert lista.tamanho == 3

def test_remover(lista):
    assert lista.remover(1) == True
    assert str(lista) == "10 -> 30 -> 40 -> null"

    assert lista.remover(0) == True
    assert str(lista) == "30 -> 40 -> null"

    assert lista.remover(10) == False

def test_remover_item(lista):
    assert lista.remover_item(20) == True
    assert str(lista) == "10 -> 30 -> 40 -> null"

    assert lista.remover_item(40) == True
    assert str(lista) == "10 -> 30 -> null"

    assert lista.remover_item(50) == False

def test_lista_vazia():
    lista0 = Lista_Ligada()

    assert lista0.pesquisar(10) == False
    assert lista0.obter(0) == None
    assert lista0.remover_inicio() == None
    assert lista0.remover(0) == False
    assert lista0.remover_item(10) == False
    assert str(lista0) == "null"

if __name__ == "__main__":
    pytest.main(["-v"])
