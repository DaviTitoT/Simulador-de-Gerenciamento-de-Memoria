class Processo:
    def __init__(self, identificador):
        self.identificador = identificador

    def __repr__(self):
        return f"Processo({self.identificador})"

    def simular(self, entrada, fila):

        processos = entrada.split()

        paginacao = None
        fila_anterior = None
        hit_miss = None
        fila_atual = None
        substituicao = None

        for p in processos:
            paginacao = p
            print(f"Paginação: {paginacao}")

            fila_anterior = fila.listar()
            print(f"Fila anterior: {fila_anterior}")

            if fila.contem(p):
                hit_miss = "HIT"
                prin
                print(f"Fila atual: {fila.listar()}")
                print("Substituição: Sim\n")
                continue
            processo = Processo(p)
            fila.adicionar(processo)
            print("MISS")
            print(f"Fila atual: {fila.listar()}")
            print("Substituição: Não\n")

