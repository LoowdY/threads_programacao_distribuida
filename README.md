
# 🧵 Projeto de Programação Paralela e Distribuída

**Aluno:** João Renan Santanna Lopes  
**Professor:** Fábio Araújo  
**Disciplina:** Programação Paralela e Distribuída

Este repositório contém a implementação das três questões propostas para a avaliação prática, envolvendo conceitos de multithreading, filas seguras, pipeline de processamento e sistemas distribuídos com comunicação via socket TCP.

---

## 📁 Estrutura de Diretórios

```
processador_threads/
├── questao1/                      # Thread pool com dispatcher e workers
├── questao2/processador_pipeline/ # Pipeline de 3 estágios com benchmarking
├── questao3/                      # Scheduler distribuído com nós via TCP
└── .gitignore
```

---

## ❓ Questões Implementadas

### ✅ Questão 1 – Thread Pool com Dispatcher

**Descrição:**  
Implementação de um sistema de processamento local com múltiplas threads, onde um `dispatcher` distribui arquivos de texto para `workers`, que realizam contagem de palavras. Utiliza `locks` para sincronização de acesso à fila compartilhada.

**Objetivo:**  
Medir o throughput (arquivos por segundo) variando o número de threads: 1, 2, 4, 8.

**Local:**  
`processador_threads/questao1/`

---

### ✅ Questão 2 – Pipeline de Três Estágios

**Descrição:**  
Reestruturação da questão anterior como pipeline com três estágios:
1. Leitura de arquivos (`threads leitoras`)
2. Processamento (normalização do texto) (`threads processadoras`)
3. Gravação de arquivos (`threads gravadoras`)

**Objetivo:**  
Avaliar a **latência total** (tempo do início ao fim do pipeline) e a **escalabilidade** ao variar o número de threads por estágio.  
Inclui benchmarking com geração de gráfico usando `matplotlib`.

**Local:**  
`processador_threads/questao2/processador_pipeline/`

---

### ✅ Questão 3 – Scheduler Distribuído com Sockets TCP

**Descrição:**  
Desenvolvimento de um sistema distribuído com um **scheduler central** e **nós remotos simulados via processos**. A comunicação é feita por socket TCP com mensagens no formato JSON.

**Funcionalidades:**
- Scheduler mantém nós `idle` e `busy`
- Recebe tarefas (nomes de arquivos)
- Envia o código e recebe resultados dos workers
- Processa beats periódicos dos nós para saber se estão disponíveis

**Objetivo:**  
Distribuir dinamicamente tarefas para nós remotos, simulando um ambiente distribuído real.

**Local:**  
`processador_threads/questao3/`

---

## ✅ Requisitos

- Python 3.7+
- Biblioteca extra para benchmark gráfico:
  ```bash
  pip install matplotlib
  ```

---

## ✍️ Observações

Todos os experimentos podem ser testados executando os arquivos principais de cada pasta:

- `questao1/`: `python processador.py`
- `questao2/`: `python benchmark_pipeline.py`
- `questao3/`: 
  - Inicie o scheduler: `python scheduler.py`
  - Inicie os workers: `python worker_node.py`


