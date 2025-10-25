from collections import defaultdict

def separar_e_somar(lista):
    """
    Recebemos aqui uma lista de strings no formato 'Letra:Valor' e retornamos
    um dicionário com a soma dos valores por letra.
    """
    resultado = defaultdict(int)
    for item in lista:
        letra, numero = item.split(":")
        resultado[letra] += int(numero)
    return dict(resultado)


def ordenar_resultado(dicionario):
    """
    Recebemos um dicionário e retornamos uma lista das chaves
    ordenadas em ordem alfabética.
    """
    return sorted(dicionario.keys())


def formatar_resultado(dicionario, letras_ordenadas):
    """
    Recebemos aqui o dicionário e a lista de letras ordenadas e retornamos
    a lista final no formato 'Letra:Soma'.
    """
    return [f"{letra}:{dicionario[letra]}" for letra in letras_ordenadas]


def somar_por_letra(lista):
    """
    Função principal que combina as funções auxiliares
    e retorna a lista final ordenada.
    """
    soma_por_letra = separar_e_somar(lista)
    letras_ordenadas = ordenar_resultado(soma_por_letra)
    resultado_final = formatar_resultado(soma_por_letra, letras_ordenadas)
    return resultado_final
