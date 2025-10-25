from dominio.processo import Processo
from dominio.fila import Fila

def main():

    processo = Processo(None)
    tamanho = int(input("Digite o tamanho máximo da moldura: "))
    fila = Fila(tamanho)
    entrada = input("Digite os acessos (ex: 1 2 33 14 2 6): ")
    processo.simular(entrada, fila)

if __name__ == "__main__":
    main()
