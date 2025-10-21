class Processo:
    def __init__(self, identificador):
        self.identificador = identificador

    def __repr__(self):
        return f"Processo({self.identificador})"

    def simular(self, entrada, fila):
        if " " in entrada:
            processos = entrada.split()
        else:
            processos = list(entrada)
   
        for p in processos:
            if fila.contem(p):
                continue 
            processo = Processo(p)
            fila.adicionar(processo)
            print(f"Fila atual: {fila.listar()}")