# A SIMPLE GUIDE 


# SYSTEM REQUIREMENTS

- python 3+
- vscode
- java 17+
- 
extensions:
- Python language support for vscode 
- Python Indent
- Python Environment Manager
- something for java debug/ build



## commits pattern

<https://www.conventionalcommits.org/en/v1.0.0/>

## Problem Details for HTTP APIs

<https://datatracker.ietf.org/doc/html/rfc7807>


## Conventional Commits micro guide

- `feat`: Addition of a new feature or functionality to the project.
- `fix`: Correction of an existing bug or issue in the code.
- `docs`: Changes to documentation, such as README updates, code comments, or API documentation.
- `style`: Changes that do not affect the code logic, such as formatting, indentation, adding whitespace, or styling changes.
- `refactor`: Refactoring of existing code, without changing functional behavior.
- `test`: Addition or modification of tests, including unit tests, integration tests, or adjustments to test scripts.
- `chore`: Maintenance tasks, configuration adjustments, dependency updates, or any other changes that do not fit into the previous categories.


# BUILD PYTHON
  

A biblioteca NetworkX (`networkx`) e Matplotlib (`matplotlib`) são as principais bibliotecas externas utilizadas nesse código. 
Se elas não estiverem instaladas no seu ambiente Python, você precisará instalá-las. 
Aqui estão os comandos para instalar essas bibliotecas:

### Instalando NetworkX e Matplotlib

1. **NetworkX**:
    ```sh
    pip install networkx
    ```

2. **Matplotlib**:
    ```sh
    pip install matplotlib
    ```

### Verificando as Instalações

Para garantir que as bibliotecas estão instaladas corretamente, você pode executar os seguintes comandos no Python:

```python
import networkx as nx
import matplotlib.pyplot as plt

print(f"NetworkX version: {nx.__version__}")
print(f"Matplotlib version: {plt.__version__}")
```

### Instruções Completas

Aqui está o conjunto completo de instruções para configurar o seu ambiente, incluindo a instalação das bibliotecas necessárias e a execução do código atualizado:

1. **Crie um novo ambiente virtual (opcional, mas recomendado)**:
    ```sh
    python -m venv myenv
    ```

2. **Ative o ambiente virtual**:
    - **Windows**:
        ```sh
        myenv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```sh
        source myenv/bin/activate
        ```

3. **Instale as bibliotecas necessárias**:
    ```sh
    pip install networkx matplotlib pydot
    ```

4. **Verifique as instalações**:
    ```sh
    python
    >>> import networkx as nx
    >>> import matplotlib.pyplot as plt
    >>> print(f"NetworkX version: {nx.__version__}")
    >>> print(f"Matplotlib version: {plt.__version__}")
    ```

5. **Execute o seu código**:
    ```sh
    python Matrioska.py
    ```

    
# RESULTS
python results:
10 = 4  0.00 ms
20 = 5  5.01 ms
50 = 11 30.36 ms
100 = 13 159.48 ms 
200 = 17 990.17 ms 
300 = 13 164.95 ms
500 = 27 15105.01 ms 
1000 = 32 110534.41 ms
limite de tempo, travando máquina... não serão executados os testes maiores

java results:
10 = 4  6 ms
20 = 5  4 ms
50 = 11 6 ms
100 = 13 40 ms 
200 = 17 42 ms 
300 = 13 13 ms
500 = 27 194 ms 
1000 = 32 295 ms
2000 = 43 380 ms
5000 = 60 1114 ms 
10000 = 75 3898 ms
