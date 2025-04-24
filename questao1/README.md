
# 🧵 Sistema de Processamento Paralelo com Thread Pool

Este projeto implementa um sistema de processamento local baseado em **thread pool**, com o objetivo de ler arquivos texto, contar as palavras e salvar os resultados de forma concorrente. Ele também permite realizar **benchmark de desempenho** variando o número de threads.

---

## 📁 Estrutura do Projeto

```
processador_threads/
├── entrada/               # Arquivos .txt de entrada
├── saida/                 # Arquivos processados com sufixo .out
├── processador.py         # Módulo principal com a função de processamento
├── benchmark.py           # Script de benchmark com geração de gráfico
├── grafico_benchmark.png  # Gráfico gerado após execução do benchmark
└── requisitos.txt         # Dependências (ex: matplotlib)
```

---

## ⚙️ Como funciona

### `processador.py`

- Utiliza múltiplas **threads (workers)** para processar arquivos concorrente.
- Cada thread:
  - Lê um arquivo `.txt`
  - Conta a frequência de palavras
  - Grava o resultado em `saida/arquivo.txt.out`
- Proteção de contador com `threading.Lock`
- Mede o tempo total e calcula o **throughput** (arquivos/segundo)

### `benchmark.py`

- Usa `argparse` para passar o número de threads via linha de comando:
  ```bash
  python benchmark.py --threads 1 2 4 8
  ```
- Executa o processamento para cada configuração
- Mede desempenho
- Gera um gráfico com `matplotlib` mostrando o throughput

---

## 📦 Instalação

1. Crie um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install matplotlib
   ```

---

## 🧪 Executando

Coloque arquivos `.txt` na pasta `entrada/`.

### Execução padrão:
```bash
python processador.py
```

### Benchmark:
```bash
python benchmark.py --threads 1 2 4 8
```

---

## 📊 Exemplo de saída:

```
▶ Rodando benchmark com 4 thread(s)...
⏱️  Tempo: 2.31s | Arquivos: 100 | Throughput: 43.29 arq/s
```

---

## 🖼️ Gráfico

Será gerado automaticamente ao final da execução do benchmark e salvo como `grafico_benchmark.png`.
