# fifo.py

from collections import deque


class FIFO:
    """Implementa o algoritmo de substituição FIFO."""

    def __init__(self, tamanho):
        self.fila = deque(maxlen=tamanho)

    def adicionar(self, pagina):
        self.fila.append(pagina)

    def remover_antiga(self):
        if self.fila:
            return self.fila.popleft()
        return None

    def contem(self, pagina):
        return pagina in self.fila

    def __repr__(self):
        return f"Fila FIFO: {list(self.fila)}"
