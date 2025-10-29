# tabela_paginas.py

class TabelaPaginas:
    """Gerencia a tabela de páginas, incluindo o bit de presença."""
    
    def __init__(self, tamanho_virtual):
        # Cada página tem: moldura (ou None) e bit de presença
        self.tabela = [
            {"pagina": i, "moldura": None, "presente": False}
            for i in range(tamanho_virtual)
        ]

    def atualizar(self, pagina, moldura, presente):
        self.tabela[pagina]["moldura"] = moldura
        self.tabela[pagina]["presente"] = presente

    def obter_moldura(self, pagina):
        return self.tabela[pagina]["moldura"]

    def esta_presente(self, pagina):
        return self.tabela[pagina]["presente"]

    def __repr__(self):
        linhas = [f"{e['pagina']:>2} | Moldura: {e['moldura']} | Presente: {e['presente']}" for e in self.tabela]
        return "\n".join(linhas)
