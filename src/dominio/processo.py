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
                print(f"Hit/Miss: {hit_miss}")

                fila_atual = fila.listar()
                print(f"Fila atual: {fila_atual}")

                substituicao = "Não"
                print(f"Substituição: {substituicao}\n")
                continue

            processo = Processo(p)
            fila.adicionar(processo)

            hit_miss = "MISS"
            print(f"Hit/Miss: {hit_miss}")

            fila_atual = fila.listar()
            print(f"Fila atual: {fila_atual}")

            substituicao = "Sim"
            print(f"Substituição: {substituicao}\n")

