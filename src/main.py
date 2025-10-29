# main.py
"""Arquivo principal — controla a simulação completa."""


from dominio.memoria_virtual import MemoriaVirtual
from dominio.memoria_fisica import MemoriaFisica
from dominio.tabela_paginas import TabelaPaginas
from dominio.fifo import FIFO
from dominio.utils import exibir_estado


def simular_fifo(tam_virtual, tam_fisica, acessos):
    memoria_virtual = MemoriaVirtual(tam_virtual)
    memoria_fisica = MemoriaFisica(tam_fisica)
    tabela = TabelaPaginas(tam_virtual)
    fifo = FIFO(tam_fisica)
    falhas = 0
    passo = 0

    for pagina in acessos:
        passo += 1
        if not tabela.esta_presente(pagina):
            falhas += 1
            print(f"⚠️ Falha de página ao acessar {pagina}")

            if memoria_fisica.esta_cheia():
                pagina_removida = fifo.remover_antiga()
                tabela.atualizar(pagina_removida, None, False)
                memoria_fisica.remover_pagina(pagina_removida)
                print(f"Página {pagina_removida} removida (FIFO)")

            posicao_livre = memoria_fisica.frames.index(None)
            memoria_fisica.adicionar_pagina(pagina, posicao_livre)
            tabela.atualizar(pagina, posicao_livre, True)
            fifo.adicionar(pagina)
        else:
            print(f"✅ Página {pagina} já está na memória.")

        exibir_estado(passo, pagina, memoria_fisica, fifo, tabela)

    print(f"\nTotal de falhas de página: {falhas}\n")


if __name__ == "__main__":
    # Exemplo de simulação
    tamanho_virtual = 8
    tamanho_fisico = 3
    acessos = [0, 2, 1, 3, 0, 4, 2, 3, 0, 1]

    simular_fifo(tamanho_virtual, tamanho_fisico, acessos)
