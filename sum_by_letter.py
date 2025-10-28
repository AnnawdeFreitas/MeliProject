from collections import defaultdict

def separar_e_somar(lista):
    """
    Recebe uma lista de strings no formato 'Letra:Valor' e retorna
    um dicionário com a soma dos valores por letra.

    - Ignora entradas inválidas (sem ':', com valores não numéricos, etc.)
    - Trata letras maiúsculas e minúsculas como iguais (A == a)
    - Exibe mensagens de aviso para facilitar o debug

    Exemplo:
        Entrada: ['A:1', 'a:2', 'B:3', 'b:x', 'C10']
        Saída:   {'A': 3, 'B': 3}
    """
    # defaultdict(int) cria um dicionário que começa com valor 0 por padrão
    # Assim, podemos somar direto sem precisar inicializar cada chave
    resultado = defaultdict(int)

    # Iteramos sobre cada item da lista recebida
    for item in lista:

        if not isinstance(item, str):
            print(f"Ignorado: item '{item}' não é uma string.")
            continue

        try:
            # Tentamos dividir a string em duas partes no primeiro ":"
            # Exemplo: "A:10" → ["A", "10"]
            # O parâmetro "1" evita erro caso haja mais de um ":", por exemplo ["A:1:2"], nesse caso estamos assumindo
            # que o primeiro valor é o que realmente pertence.
            letra, numero = item.split(":", 1)

            # Remove espaços em branco ao redor
            letra = letra.strip()
            numero = numero.strip()

            # Normaliza a letra para MAIÚSCULA (para tratar 'a' e 'A' como iguais)
            letra = letra.upper()

            # Converte o número (string) para inteiro
            numero = int(numero)

            # Soma o valor correspondente à letra no dicionário
            resultado[letra] += numero

        except ValueError:
            # ValueError ocorre em duas situações principais:
            # quando falta o ":" → item.split() não consegue separar
            # pu o valor numérico não é um número válido
            if ":" not in str(item):
                print(f"Aviso: entrada inválida (sem separador ':') → {item}")
            else:
                print(f"Aviso: valor numérico inválido → {item}")
            # Ignoramos o item e seguimos para o próximo
            continue

        except TypeError:
            # TypeError ocorre quando o item não é uma string (ex: None, int)
            print(f"Aviso: item não é string → {item}")
            continue

    # Convertendo o defaultdict para dict antes de retornar
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
