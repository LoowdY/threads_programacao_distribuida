
# 🧵 Pipeline Multithread para Processamento de Arquivos

Este projeto implementa um sistema de processamento distribuído em **3 estágios**, com threads dedicadas por estágio e comunicação via **filas seguras**.

---

## 📁 Estrutura

```
processador_pipeline/
├── entrada/                 # Arquivos de entrada (.txt)
├── saida/                   # Arquivos de saída (.out)
├── processador_pipeline.py  # Lógica principal do pipeline
├── benchmark_pipeline.py    # Script de benchmark com gráfico
├── benchmark_pipeline.png   # Gráfico gerado (após execução)
└── README.md
```

---

## 🔁 Estágios do Pipeline

1. **Leitura**: Threads leem os arquivos e colocam texto bruto na fila.
2. **Processamento**: Threads pegam o texto e aplicam normalização.
3. **Gravação**: Threads salvam o texto em arquivos `.out`.

---

## 🚀 Como Executar

1. Coloque arquivos `.txt` na pasta `entrada/`
2. Rode o script principal:

```bash
python processador_pipeline.py
```

---

## 📊 Benchmark

1. Rode o benchmark com:

```bash
python benchmark_pipeline.py
```

2. O gráfico `benchmark_pipeline.png` será gerado automaticamente comparando a latência para diferentes números de threads por estágio.

---

## ✅ Requisitos

```bash
pip install matplotlib
```