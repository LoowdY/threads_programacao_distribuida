import os
import argparse
import matplotlib.pyplot as plt
from processador import executar_processamento

def classificar_arquivos_por_tamanho(pasta):
    arquivos = [(f, os.path.getsize(os.path.join(pasta, f))) for f in os.listdir(pasta) if f.endswith('.txt')]
    arquivos.sort(key=lambda x: x[1])
    return [os.path.join(pasta, nome) for nome, _ in arquivos]

def executar_benchmark(pasta_entrada, pasta_saida, threads_lista):
    resultados = []

    for n_threads in threads_lista:
        print(f"\n▶ Rodando benchmark com {n_threads} thread(s)...")
        arquivos = classificar_arquivos_por_tamanho(pasta_entrada)
        arquivos_processados, duracao, throughput = executar_processamento(pasta_entrada, pasta_saida, n_threads)
        print(f"⏱️  Tempo: {duracao:.2f}s | Arquivos: {arquivos_processados} | Throughput: {throughput:.2f} arq/s")
        resultados.append((n_threads, throughput))

    return resultados

def plotar_resultados(resultados):
    threads, throughputs = zip(*resultados)
    plt.figure(figsize=(10, 6))
    plt.plot(threads, throughputs, marker='o')
    plt.title("Benchmark: Threads vs Throughput")
    plt.xlabel("Número de Threads")
    plt.ylabel("Throughput (arquivos/segundo)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_benchmark.png")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark de processamento com múltiplas threads")
    parser.add_argument("--entrada", default="entrada", help="Pasta de entrada")
    parser.add_argument("--saida", default="saida", help="Pasta de saída")
    parser.add_argument("--threads", nargs="+", type=int, default=[1, 2, 4, 8], help="Lista de quantidades de threads")

    args = parser.parse_args()
    resultados = executar_benchmark(args.entrada, args.saida, args.threads)
    plotar_resultados(resultados)
