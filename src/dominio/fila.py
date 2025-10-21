from collections import deque

class Fila:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.fila = deque(maxlen=tamanho_maximo)

    def adicionar(self, processo):
        """Adiciona um processo à fila, removendo o mais antigo se estiver cheia."""
        self.fila.append(processo)

    def remover(self):
        """Remove o primeiro processo (FIFO)."""
        if self.fila:
            return self.fila.popleft()
        return None

    def listar(self):
        """Retorna a fila atual como lista."""
        return list(self.fila)

    def contem(self, identificador):
        """Verifica se um processo com o dado identificador está na fila."""
        return any(processo.identificador == identificador for processo in self.fila)
    
    def __repr__(self):
        return f"Fila({list(self.fila)})"
