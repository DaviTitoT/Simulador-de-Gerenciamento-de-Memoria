# utils.py
"""Funções auxiliares, como exibição de estado e formatação."""


def exibir_estado(passo, pagina, memoria_fisica, fifo, tabela):
    print("\n" + "="*50)
    print(f"Passo {passo} — Acesso à página {pagina}")
    print(memoria_fisica)
    print(fifo)
    print("Tabela de Páginas:")
    print(tabela)
    print("="*50 + "\n")
