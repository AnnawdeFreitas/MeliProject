import pytest
from sum_by_letter import separar_e_somar, ordenar_resultado, formatar_resultado, somar_por_letra

# TEstando entradas invalidas

def test_entrada_sem_separador():
    entrada = ["A1", "B:2"]
    # 'A1' deve ser ignorado, somando apenas 'B:2'
    esperado = {"B": 2}
    assert separar_e_somar(entrada) == esperado


def test_valor_nao_numerico():
    entrada = ["A:x", "B:2"]
    # 'A:x' deve ser ignorado, 'B:2' processado
    esperado = {"B": 2}
    assert separar_e_somar(entrada) == esperado


def test_item_nao_string():
    entrada = ["A:1", None, 123, "B:2"]
    # None e 123 devem ser ignorados
    esperado = {"A": 1, "B": 2}
    assert separar_e_somar(entrada) == esperado


def test_entrada_vazia():
    entrada = []
    esperado = []
    assert somar_por_letra(entrada) == esperado


# Testando formatação e normalização

def test_letras_minusculas_e_maiusculas():
    entrada = ["a:1", "A:2", "b:3", "B:4"]
    # Deve somar 'a' e 'A' juntos, idem para 'b' e 'B'
    esperado = ["A:3", "B:7"]
    assert somar_por_letra(entrada) == esperado


def test_espacos_em_branco():
    entrada = [" A : 1 ", " B:2", "C :3 "]
    # Espaços não devem afetar o resultado
    esperado = ["A:1", "B:2", "C:3"]
    assert somar_por_letra(entrada) == esperado


def test_separador_extra():
    entrada = ["A:1:2", "B:3"]
    # "A:1:2" deve ser ignorado por formato incorreto
    esperado = ["B:3"]
    assert somar_por_letra(entrada) == esperado


# Testandoi valores numericos

def test_valores_negativos_e_zero():
    entrada = ["A:-2", "B:0", "A:3"]
    # Soma: A = 1, B = 0
    esperado = ["A:1", "B:0"]
    assert somar_por_letra(entrada) == esperado


def test_valores_grandes():
    entrada = ["A:999999999999999999", "A:1"]
    # Deve somar sem erro, pois Python suporta inteiros grandes
    esperado = ["A:1000000000000000000"]
    assert somar_por_letra(entrada) == esperado


# testando a ordenação

def test_ordenar_resultado_com_muitas_letras():
    dicionario = {"Z": 1, "C": 2, "A": 3, "B": 4}
    esperado = ["A", "B", "C", "Z"]
    assert ordenar_resultado(dicionario) == esperado


# Testando a formação final

def test_formatar_resultado_com_valores_negativos():
    dicionario = {"A": -1, "B": 0, "C": 10}
    letras_ordenadas = ["A", "B", "C"]
    esperado = ["A:-1", "B:0", "C:10"]
    assert formatar_resultado(dicionario, letras_ordenadas) == esperado