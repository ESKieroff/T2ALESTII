Resultados da implementação python:
Caso	tempo 
10		0.00 ms
20 		5.01 ms
50		30.36 ms
100		159.48 ms 
200		990.17 ms 
300		164.95 ms
500		15105.01 ms 
1000	110534.41 ms
-- não foi possível executar além deste. 

Resultados da implementação java:
Caso	tempo 
10		6 ms
20		4 ms
50		6 ms
100		40 ms 
200		42 ms 
300		13 ms
500		194 ms 
1000	295 ms
2000	380 ms
5000	1114 ms 
10000	3898 ms


![grafico comparativo](/comparativo%20execução%20programas.png)

Aqui está o gráfico comparando os tempos de execução dos programas em Python e Java para diferentes tamanhos de entrada. Usamos uma escala logarítmica tanto para os tamanhos de entrada quanto para os tempos de execução, o que ajuda a visualizar melhor a ampla variação dos dados. 


### Panorama Geral sobre a Complexidade dos Algoritmos

### Pseudocódigo em Portugol

#### Primeiro Código (Java)

**Descrição Geral**:
- Lê uma lista de caixas de um arquivo e determina a sequência mais longa de caixas que podem ser encaixadas uma dentro da outra.
- Constrói um grafo direcionado onde cada nó representa uma caixa e cada aresta indica que uma caixa pode ser encaixada dentro de outra.
- Encontra o caminho mais longo no grafo, que representa a sequência mais longa de caixas encaixáveis.

**Pseudocódigo**:

```portugol
programa Matrioska
    variáveis
        lista caixas
        mapa grafo

    procedimento principal()
        inicio = tempo_atual()
        lerCaixasDeArquivo("teste.txt")
        construirGrafo()
        caminhoMaisLongo = encontrarCaminhoMaisLongo()
        fim = tempo_atual()
        tempoExecucao = fim - inicio
        escrever("O maior número de caixas encaixáveis é: ", comprimento(caminhoMaisLongo))
        escrever("Tempo de execução: ", tempoExecucao, " ms")
        escreverLog(caminhoMaisLongo, "log.txt")
        exportarGrafoDot("grafo.dot")
        exportarCaminhoMaisLongoDot(caminhoMaisLongo, "caminho_mais_longo.dot")

    procedimento lerCaixasDeArquivo(nomeArquivo)
        abrirArquivo(nomeArquivo)
        enquanto linha = lerLinha() diferente de nulo
            partes = dividir(linha, " ")
            se comprimento(partes) != 3 então
                erro("Formato inválido: cada linha deve conter exatamente 3 inteiros")
            dimensoes = converterParaInteiros(partes)
            adicionarCaixa(caixas, criarCaixa(dimensoes))
        fecharArquivo()
        ordenarCaixas(caixas)

    procedimento construirGrafo()
        para cada caixa em caixas
            adicionarNodo(grafo, caixa)
            para cada outraCaixa em caixas
                se caixa diferente de outraCaixa e outraCaixa.cabeDentro(caixa)
                    adicionarAresta(grafo, outraCaixa, caixa)

    função encontrarCaminhoMaisLongo()
        mapa memo
        mapa predecessor
        maiorCaminho = []
        para cada caixa em caixas
            comprimentoCaminho, caminho = dfs(caixa, memo, predecessor)
            se comprimento(caminho) > comprimento(maiorCaminho)
                maiorCaminho = caminho
        retornar maiorCaminho

    função dfs(caixa, memo, predecessor)
        se caixa está em memo
            retornar memo[caixa]
        comprimentoMaximo = 1
        melhorPredecessor = nulo
        para cada vizinho em grafo[caixa]
            comprimento, _ = dfs(vizinho, memo, predecessor)
            se comprimento + 1 > comprimentoMaximo
                comprimentoMaximo = comprimento + 1
                melhorPredecessor = vizinho
        memo[caixa] = (comprimentoMaximo, melhorPredecessor)
        retornar (comprimentoMaximo, melhorPredecessor)

    procedimento escreverLog(caminho, nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        para cada caixa em caminho
            escreverLinha(caixa)
        fecharArquivo()

    procedimento exportarGrafoDot(nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        escrever("digraph G {")
        para cada caixa em grafo
            para cada vizinho em grafo[caixa]
                escrever(" ", caixa.id, " -> ", vizinho.id, ";")
        escrever("}")
        fecharArquivo()

    procedimento exportarCaminhoMaisLongoDot(caminho, nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        escrever("digraph G {")
        para i = 0 até comprimento(caminho) - 2
            escrever(" ", caminho[i].id, " -> ", caminho[i + 1].id, ";")
        escrever("}")
        fecharArquivo()
```

#### Segundo Código (Python)

**Descrição Geral**:
- Lê uma lista de caixas de um arquivo e determina a sequência mais longa de caixas que podem ser encaixadas uma dentro da outra.
- Constrói um grafo direcionado onde cada nó representa uma caixa e cada aresta indica que uma caixa pode ser encaixada dentro de outra.
- Verifica se o grafo contém ciclos.
- Encontra o caminho mais longo no grafo, que representa a sequência mais longa de caixas encaixáveis.

**Pseudocódigo**:

```portugol
programa Matrioska
    variáveis
        lista caixas
        grafo

    procedimento principal()
        inicio = tempo_atual()
        lerCaixasDeArquivo("teste.txt")
        construirGrafo()
        se verificarCiclos()
            escrever("O grafo contém ciclos. Verifique os dados de entrada.")
            retornar
        caminhoMaisLongo = encontrarCaminhoMaisLongo()
        fim = tempo_atual()
        tempoExecucao = (fim - inicio) * 1000
        escrever("O maior número de caixas encaixáveis é: ", comprimento(caminhoMaisLongo))
        escrever("Tempo de execução: ", tempoExecucao, " ms")
        escreverLog(caminhoMaisLongo, "log.txt")
        exportarGrafoDot("grafo.dot")
        exportarCaminhoMaisLongoDot(caminhoMaisLongo, "caminho_mais_longo.dot")

    procedimento lerCaixasDeArquivo(nomeArquivo)
        abrirArquivo(nomeArquivo)
        índice = 1
        enquanto linha = lerLinha() diferente de nulo
            partes = dividir(linha, " ")
            se comprimento(partes) != 3 então
                erro("Formato inválido: cada linha deve conter exatamente 3 inteiros")
            dimensoes = converterParaInteiros(partes)
            adicionarCaixa(caixas, criarCaixa(dimensoes, índice))
            índice = índice + 1
        fecharArquivo()
        ordenarCaixas(caixas)

    procedimento construirGrafo()
        para cada caixa em caixas
            adicionarNodo(grafo, caixa.id, caixa.dimensoes)
        para i = 0 até comprimento(caixas) - 1
            para j = i + 1 até comprimento(caixas)
                se caixas[j].cabeDentro(caixas[i])
                    adicionarAresta(grafo, caixas[j].id, caixas[i].id)

    função verificarCiclos()
        tentar
            ciclos = encontrarCiclos(grafo)
            retornar verdadeiro se ciclos então
        exceto NenhumCicloEncontrado
            retornar falso

    função encontrarCaminhoMaisLongo()
        mapa memo
        maiorCaminho = []
        para cada caixaId em nós(grafo)
            comprimentoCaminho, caminho = dfs(caixaId, memo)
            se comprimento(caminho) > comprimento(maiorCaminho)
                maiorCaminho = caminho
        retornar maiorCaminho

    função dfs(caixaId, memo)
        se caixaId está em memo
            retornar memo[caixaId]
        comprimentoMaximo = 1
        caminhoMaximo = [caixaId]
        para cada vizinhoId em vizinhos(grafo, caixaId)
            comprimento, caminho = dfs(vizinhoId, memo)
            se comprimento + 1 > comprimentoMaximo
                comprimentoMaximo = comprimento + 1
                caminhoMaximo = [caixaId] + caminho
        memo[caixaId] = (comprimentoMaximo, caminhoMaximo)
        retornar memo[caixaId]

    procedimento escreverLog(caminho, nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        para cada caixaId em caminho
            dimensoes = obterDimensoes(grafo, caixaId)
            escreverLinha(caixaId, dimensoes)
        fecharArquivo()

    procedimento exportarGrafoDot(nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        escrever("digraph G {")
        para cada caixaId em nós(grafo)
            para cada vizinhoId em vizinhos(grafo, caixaId)
                escrever(" ", caixaId, " -> ", vizinhoId, ";")
        escrever("}")
        fecharArquivo()

    procedimento exportarCaminhoMaisLongoDot(caminho, nomeArquivo)
        abrirArquivoParaEscrita(nomeArquivo)
        escrever("digraph G {")


        para i = 0 até comprimento(caminho) - 2
            escrever(" ", caminho[i], " -> ", caminho[i + 1], ";")
        escrever("}")
        fecharArquivo()
```

### Complexidade dos Algoritmos

**Primeiro Código (Java)**:
1. **Leitura e Ordenação das Caixas**: O(n log n), onde n é o número de caixas.
2. **Construção do Grafo**: O(n^2), pois verifica se cada caixa cabe em cada outra.
3. **Busca do Caminho Mais Longo (DFS)**: O(n + e), onde n é o número de nós (caixas) e e é o número de arestas no grafo. No pior caso, e pode ser O(n^2).

**Segundo Código (Python)**:
1. **Leitura e Ordenação das Caixas**: O(n log n), onde n é o número de caixas.
2. **Construção do Grafo**: O(n^2), pois verifica se cada caixa cabe em cada outra.
3. **Verificação de Ciclos**: O(n + e), onde n é o número de nós e e é o número de arestas.
4. **Busca do Caminho Mais Longo (DFS)**: O(n + e).

Ambos os algoritmos têm complexidade geral aproximadamente O(n^2) devido à construção do grafo. A principal diferença é a verificação de ciclos no código Python, que acaba não fazendo sentido para esta implementação em específico, porque não conseguimos inserir uma aresta para uma caixa que seja maior que outra anterior devido às restrições da regra de negócio do programa, no momento que realiza a validação entre o vértice e o próximo. 
