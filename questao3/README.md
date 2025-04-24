
# 🧠 Sistema Distribuído com Scheduler Central via TCP

Este projeto simula um sistema distribuído em que um **scheduler central** gerencia a distribuição de tarefas a **nós remotos (workers)**, utilizando **sockets TCP** e **threads/processos distintos**.

---

## 📁 Estrutura do Projeto

```
scheduler_distribuido/
├── scheduler.py            # Scheduler central (gerencia nós e tarefas)
├── worker_node.py          # Nó remoto que processa parte do pipeline
├── shared.py               # Código compartilhado (protocolo de mensagens)
├── entrada/                # Arquivos a serem processados
├── resultados/             # Resultados dos workers
└── README.md
```

---

## 📦 Tecnologias Utilizadas

- `socket` TCP (comunicação)
- `threading` (concorrência)
- `multiprocessing` (simulação de nós)
- `json` (formato de mensagens)

---

## 🔗 Protocolo de Comunicação (mensagens JSON)

- `BEAT`: batida periódica para indicar que o nó está vivo
- `READY`: (não usado ainda) disponibilidade
- `PROCESS`: tarefa enviada ao nó
- `RESULT`: resultado da tarefa enviado de volta ao scheduler

---

## 🚀 Execução

### 1. Inicie o Scheduler:

```bash
python scheduler.py
```

> Ele escuta por conexões, recebe tarefas da pasta `entrada/`, e gerencia a distribuição.

### 2. Inicie um ou mais Workers:

```bash
python worker_node.py
```

> Cada worker se conecta ao scheduler, recebe uma tarefa e envia o resultado processado.

---

## 📄 Exemplo de Entrada (`entrada/exemplo1.txt`)

```
O sistema distribuído é poderoso.
O scheduler deve balancear a carga entre nós.
```

## 📤 Exemplo de Saída (`resultados/exemplo1.txt.out`)

```
o sistema distribuído é poderoso.
o scheduler deve balancear a carga entre nós.
```

---

## 🔁 Comportamento do Sistema

- Os workers se conectam e enviam “beats” regularmente.
- O scheduler mantém listas de workers `idle` e `busy`.
- Ao receber tarefas, ele as despacha para nós `idle`.
- O resultado é salvo em `resultados/`.

---

## ✅ Requisitos

- Python 3.7+
- Nada além da biblioteca padrão (`socket`, `threading`, `json`, `os`)

