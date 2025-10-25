# SumPorLetra

Projeto em **Python** que consolida e soma valores por letra a partir de uma lista de strings no formato `"Letra:Valor"`.
O resultado é retornado como uma lista de strings **ordenada alfabeticamente**, no formato `"Letra:Soma"`.

---

## 📝 Motivação

Durante uma entrevista de live coding, fiquei um pouco **nervosa** e não consegui apresentar a solução completa ao vivo.
Decidi finalizar o desafio agora para:

- Me sentir **mais confiante** com o resultado do meu trabalho.
- Mostrar uma **possível solução** de forma organizada e testável para os avaliadores.

Agradeço muito a oportunidade de participar do processo, independentemente do resultado.

---

## ⚙️ Funcionalidades

- Consolida valores por letra, mesmo que apareçam múltiplas vezes.
- Ordena a saída alfabeticamente.
- Código modular e testável, seguindo princípios de **DRY** (Don't Repeat Yourself).
- Contêiner Docker pronto para rodar sem precisar configurar Python.

---

## 🛠️ Como usar

### Rodar localmente

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/AnnawdeFreitas/MeliProject](https://github.com/AnnawdeFreitas/MeliProject)
    cd MeliProject
    ```

2.  Instale as dependências (opcional, apenas `pytest` se for rodar os testes):

    ```bash
    pip install pytest
    ```

3.  Execute o código principal:

    ```bash
    python sum_by_letter.py
    ```

4.  Execute os testes:

    ```bash
    pytest test_sum_by_letter.py
    ```

### Rodar com Docker

Certifique-se de ter o [Docker](https://www.docker.com/get-started) instalado.

1.  Construa a imagem Docker:

    ```bash
    docker build -t sum_por_letra .
    ```

2.  Execute o script principal dentro do container:

    ```bash
    docker run --rm sum_por_letra
    ```

3.  Execute os testes dentro do container:

    ```bash
    docker run --rm sum_por_letra pytest tests_sum_by_letter.py
    ```

> Todo o projeto é autocontido dentro do container, garantindo que qualquer pessoa consiga rodar sem configurar nada na máquina local.

---

## 📦 Estrutura do projeto

```bash
   MeliProject/
│
├── Dockerfile                      
├── README.md               
├── sum_by_letter.py        
└── test_sum_by_letter.py   
   ```


Ps: A formatação deste README.md foi realizada com a ajuda de IA 💛