import pytest
from sum_by_letter import separar_e_somar, ordenar_resultado, formatar_resultado, somar_por_letra

# Teste para a função separar_e_somar
def test_separar_e_somar():
    entrada = ["A:1", "B:2", "A:3"]
    esperado = {"A": 4, "B": 2}
    assert separar_e_somar(entrada) == esperado

# Teste para ordenar_resultado
def test_ordenar_resultado():
    dicionario = {"D": 7, "A": 12, "B": 1}
    esperado = ["A", "B", "D"]
    assert ordenar_resultado(dicionario) == esperado

# Teste para formatar_resultado
def test_formatar_resultado():
    dicionario = {"A": 12, "B": 1, "C": -3, "D": 7}
    letras_ordenadas = ["A", "B", "C", "D"]
    esperado = ["A:12", "B:1", "C:-3", "D:7"]
    assert formatar_resultado(dicionario, letras_ordenadas) == esperado

# Teste final da função somar_por_letra
def test_somar_por_letra():
    entrada = ["D:7", "A:1", "B:0", "A:11", "C:-3", "B:1"]
    esperado = ["A:12", "B:1", "C:-3", "D:7"]
    assert somar_por_letra(entrada) == esperado

# Testes adicionais (casos com letras repetidas e números negativos)
def test_casos_adicionais():
    entrada = ["X:5", "Y:-2", "X:3"]
    esperado = ["X:8", "Y:-2"]
    assert somar_por_letra(entrada) == esperado