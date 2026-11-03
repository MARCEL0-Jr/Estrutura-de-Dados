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
    assert "10 -> 20 -> 30 -> 40 -> null"

def test_print_str_lista(lista):
    assert "10 -> 20 -> 30 -> 40 -> null"

def test_inserir_inicio(lista):
    lista.inserir_inicio(7)
