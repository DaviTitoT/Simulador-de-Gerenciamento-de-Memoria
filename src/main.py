from dominio.processo import Processo
from dominio.fila import Fila

def main():
    
    processo = Processo(None)  
    tamanho = int(input("Digite o tamanho máximo da fila: "))
    fila = Fila(tamanho)
    entrada = input("Digite os processos (ex: 1 2 3 4 5 6 ou 123456): ")
    processo.simular(entrada, fila)

if __name__ == "__main__":
    main()
