# 🧠 Simulador de Gerenciamento de Memória com Paginação (FIFO)

## 📌 Descrição

Este projeto é uma simulação do gerenciamento de memória de um sistema operacional utilizando paginação.
O objetivo é demonstrar:

- O mapeamento de páginas virtuais para molduras físicas.
- A ocorrência de falhas de página.
- A substituição de páginas utilizando o algoritmo FIFO (First In, First Out).

## 🧰 Tecnologias

- **Linguagem:** Python 3.10+
- **Interface:** Tkinter (GUI)
- **Execução:** Aplicação gráfica interativa

## 🏗 Estrutura do Projeto

```
📁 simulador_memoria/
│
├── main.py                 # Arquivo principal - inicia a interface gráfica
│
├── dominio/                # (Lógica da simulação e estruturas de dados)
│   ├── simulador.py        # Classe Simulador (regras de paginação FIFO)
│   ├── fila.py             # Implementação manual da fila FIFO
│   ├── lista.py            # (opcional — se precisar de lista encadeada)
│   └── no.py               # Classe No (nó da estrutura)
│
├── interface/              # (Interface gráfica e apresentação)
│   └── app.py              # Classe App (Tkinter)
│
├── tests/                  # (opcional — testes unitários)
│   └── test_simulador.py
│
└── README.md               # Descrição do projeto
```

## 👥 Divisão de Tarefas (Sugestão para 4 integrantes)

- **Membro 1:** Implementação da lógica principal (`simulador.py`) e integração com a fila.
- **Membro 2:** Implementação das estruturas de dados (`fila.py`, `no.py`, `lista.py`).
- **Membro 3:** Desenvolvimento da interface gráfica (`app.py`) e conexão com o simulador.
- **Membro 4:** Testes e integração (`test_simulador.py` e `main.py`).

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Navegue até a pasta do projeto:
   ```bash
   cd simulador_memoria
   ```
3. Execute o projeto:
   ```bash
   python main.py
   ```

---

## 📚 Créditos

Projeto acadêmico para fins educacionais — Simulação de Gerenciamento de Memória (FIFO).
