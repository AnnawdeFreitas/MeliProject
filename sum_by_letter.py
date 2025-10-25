from collections import defaultdict

def somar_por_letra(lista):
    """
    Recebe uma lista de strings no formato 'Letra:Valor' e retorna um dicionário
    com a soma dos valores para cada letra.
    """

    # Cria um dicionário que já começa cada letra com 0
    # Assim podemos somar sem precisar verificar se a letra existe
    resultado = defaultdict(int)

    # Vamos percorrer cada item da lista
    for item in lista:
        # Cada item vem no formato "Letra:Numero", então a gente separa por ":"
        letra, numero = item.split(":")

        # Convertemos o num de string para inteiro e somamos ao total da letra
        resultado[letra] += int(numero)
        # Se a letra ainda não existia no dicionário, o defaultdict cria com 0
        # e já soma o valor atual automaticamente. Nesse caso o deafult dict atua como um hashmap de fato,
        # então não precisamos validar se a letra existe ou não, ele faz isso "automagicamente"

        # Agora vamos organizar as letras em ordem alfabética, a função sorted do python faz isso.
        # pode ser usado com qualquer tipo de dado
        letras_ordenadas = sorted(resultado.keys())

        # Montamos a lista final no formato "Letra:Soma", seguindo a ordem alfabética
        resultado_formatado = [f"{letra}:{resultado[letra]}" for letra in letras_ordenadas]

    return resultado_formatado


# Teste provisório:
if __name__ == "__main__":
    entrada = ["D:7", "A:1", "B:0", "A:11", "C:-3", "B:1"]
    saida = somar_por_letra(entrada)

    # Imprime a lista final, agora ordenada
    print(saida)  # Saída esperada: ['A:12', 'B:1', 'C:-3', 'D:7']
