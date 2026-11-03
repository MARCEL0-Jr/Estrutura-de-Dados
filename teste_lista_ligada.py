from lista_ligada import Lista_Ligada


def test_lista_vazia():
    lista = Lista_Ligada()

    assert lista.tamanho == 0
    assert lista.primeiro is None


def test_adicionar():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)

    assert lista.tamanho == 2


def test_exibir():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)

    assert lista.exibir() == "10 -> 20 -> null"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])