import os
import time
import matplotlib.pyplot as plt
from processador_pipeline import main as run_pipeline

def medir_tempo_pipeline(num_leitoras, num_processadoras, num_gravadoras):
    import processador_pipeline as pipeline
    pipeline.NUM_THREADS_LEITURA = num_leitoras
    pipeline.NUM_THREADS_PROCESSAMENTO = num_processadoras
    pipeline.NUM_THREADS_GRAVACAO = num_gravadoras
    inicio = time.time()
    pipeline.main()
    fim = time.time()
    return fim - inicio

def executar_benchmark_pipeline():
    # Configurações de threads: (leitoras, processadoras, gravadoras)
    configuracoes = [(1, 1, 1), (2, 2, 2), (4, 4, 4), (8, 8, 8)]
    tempos = []

    for config in configuracoes:
        print(f"🧪 Executando pipeline com {config} threads por estágio...")
        tempo = medir_tempo_pipeline(*config)
        tempos.append((config[0], tempo))  # threads por estágio, tempo total

    return tempos

def plotar_resultados(resultados):
    threads, tempos = zip(*resultados)
    plt.figure(figsize=(10, 6))
    plt.plot(threads, tempos, marker='o', linestyle='--')
    plt.title("Benchmark do Pipeline: Threads por Estágio vs Latência")
    plt.xlabel("Threads por Estágio")
    plt.ylabel("Latência Total (segundos)")
    plt.xticks(threads)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("benchmark_pipeline.png")
    plt.show()

if __name__ == "__main__":
    resultados = executar_benchmark_pipeline()
    plotar_resultados(resultados)
