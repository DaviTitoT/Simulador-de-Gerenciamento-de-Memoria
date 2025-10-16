# 🧠 Simulador de Gerenciamento de Memória com Paginação (FIFO)

## 📌 Descrição
Este projeto é uma simulação do gerenciamento de memória de um sistema operacional utilizando **paginação**.  
O objetivo é demonstrar:
- O mapeamento de páginas virtuais para molduras físicas.
- A ocorrência de falhas de página.
- A substituição de páginas utilizando o algoritmo **FIFO (First In, First Out)**.

## 🧰 Tecnologias
- Linguagem: Python 3.10+
- Execução em linha de comando (CLI)

---

## 🏗 Estrutura do Projeto

📁 simulador_memoria/
│
├── main.py                      # Arquivo principal - inicia a interface gráfica
│
├── dominio/                     # (Lógica da simulação e estruturas de dados)
│   ├── simulador.py             # Classe Simulador (regras de paginação FIFO)
│   ├── fila.py                  # Implementação manual da fila FIFO
│   ├── lista.py                 # (opcional — se precisar de lista encadeada)
│   └── no.py                    # Classe No (nó de lista/estrutura)
│
├── interface/                   # (Interface gráfica e apresentação)
│   └── app.py                   # Classe App (Tkinter)
│                    
│
├── tests/                       # (opcional — testes unitários)
│   └── test_simulador.py
│
└── README.md                    # Descrição do projeto

