# memoria_fisica.py

class MemoriaFisica:
    """Gerencia as molduras (frames) da memória física"""

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.frames = [None] * tamanho

    def esta_cheia(self):
        return None not in self.frames

    def adicionar_pagina(self, pagina, posicao):
        self.frames[posicao] = pagina

    def remover_pagina(self, pagina):
        if pagina in self.frames:
            indice = self.frames.index(pagina)
            self.frames[indice] = None

    def __repr__(self):
        return f"Memória Física: {self.frames}"
