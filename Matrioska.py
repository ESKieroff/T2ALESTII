import networkx as nx
import matplotlib.pyplot as plt
from Box import Box  # Importar a classe Box do arquivo Box.py
import time

class Matrioska:
    def __init__(self):
        self.boxes = []  # Lista para armazenar todas as caixas
        self.graph = nx.DiGraph()  # Criar um grafo direcionado usando NetworkX

    def main(self):
        start_time = time.time()  # Registrar o tempo de início

        self.read_boxes_from_file("teste.txt")  # Ler as caixas do arquivo
        self.build_graph()  # Construir o grafo com as caixas
        longest_path = self.find_longest_path()  # Encontrar o caminho mais longo no grafo

        end_time = time.time()  # Registrar o tempo de término
        execution_time = (end_time - start_time) * 1000  # Converter o tempo de execução para milissegundos

        print(f"The longest sequence of boxes is: {len(longest_path)}")  # Imprimir o comprimento do caminho mais longo
        print(f"Execution time: {execution_time:.2f} ms")  # Imprimir o tempo de execução

        self.write_log_file(longest_path, "log.txt")  # Escrever o caminho mais longo em um arquivo de log

        # Visualizar o grafo completo
        self.visualize_graph()

    def read_boxes_from_file(self, filename):
        # Abrir o arquivo para leitura
        with open(filename, 'r') as file:
            for index, line in enumerate(file):
                parts = line.strip().split()  # Dividir cada linha em partes separadas por espaços
                if len(parts) != 3:
                    raise ValueError("Invalid input format: each line must contain exactly 3 integers")
                dimensions = list(map(int, parts))  # Converter as partes em inteiros (dimensões da caixa)
                box_id = index + 1  # Definir um identificador único para cada caixa
                self.boxes.append(Box(dimensions, box_id))  # Adicionar a caixa à lista de caixas

        self.boxes.sort(reverse=True)  # Ordenar caixas em ordem decrescente

    def build_graph(self):
        # Ordenar as caixas em ordem decrescente pelo volume (opcional)
        self.boxes.sort(key=lambda box: box.dimensions[0] * box.dimensions[1] * box.dimensions[2], reverse=True)

        # Criar os vértices (nós) no grafo
        for box in self.boxes:
            self.graph.add_node(box.id, dimensions=box.dimensions)  # Adicionar um nó para cada caixa

        # Criar as arestas (ligações) no grafo
        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                if self.boxes[j].fits_inside(self.boxes[i]):  # Verificar se a caixa j cabe dentro da caixa i
                    self.graph.add_edge(self.boxes[j].id, self.boxes[i].id)  # Adicionar uma aresta de j para i

    def find_longest_path(self):
        memo = {}  # Dicionário para armazenar os caminhos já calculados
        longest_path_length = 0
        longest_path = []

        # Percorrer cada nó no grafo
        for box_id in self.graph.nodes():
            path_length, path = self.dfs(box_id, memo)  # Executar busca em profundidade (DFS) a partir do nó atual
            if path_length > longest_path_length:  # Atualizar o caminho mais longo encontrado
                longest_path_length = path_length
                longest_path = path

        return longest_path

    def dfs(self, box_id, memo):
        if box_id in memo:  # Se o caminho já foi calculado, retornar o valor armazenado
            return memo[box_id]

        max_length = 1  # O próprio box
        max_path = [box_id]

        for neighbor_id in self.graph.neighbors(box_id):  # Percorrer os vizinhos do nó atual
            length, path = self.dfs(neighbor_id, memo)  # Recursivamente executar DFS no vizinho
            if length + 1 > max_length:  # Atualizar o caminho máximo se um caminho maior for encontrado
                max_length = length + 1
                max_path = [box_id] + path

        memo[box_id] = (max_length, max_path)  # Armazenar o caminho máximo no dicionário
        return memo[box_id]

    def write_log_file(self, path, filename):
        with open(filename, 'w') as file:  # Abrir o arquivo de log para escrita
            for node_id in path:  # Escrever cada nó do caminho no arquivo
                dimensions = self.graph.nodes[node_id]['dimensions']
                file.write(f"{node_id:03d} {dimensions}\n")

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)  # Definir a disposição dos nós no gráfico
        labels = {node: f"{node} {self.graph.nodes[node]['dimensions']}" for node in self.graph.nodes()}  # Definir os rótulos dos nós
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_color='lightblue', edge_color='grey', font_weight='bold')  # Desenhar o gráfico
        plt.show()  # Exibir o gráfico
        
if __name__ == "__main__":
    matrioska = Matrioska()
    matrioska.main()
    matrioska.read_boxes_from_file("teste.txt")
    matrioska.build_graph()    
    matrioska.write_log_file("log.txt")
    matrioska.visualize_graph()
