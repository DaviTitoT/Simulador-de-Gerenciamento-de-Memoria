# memoria_virtual.py

class MemoriaVirtual:
    """Representa a memória virtual, que contém páginas numeradas"""

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.paginas = list(range(tamanho))

    def __repr__(self):
        return f"Memória Virtual: {self.paginas}"
