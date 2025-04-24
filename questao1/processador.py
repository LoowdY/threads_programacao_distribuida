import threading
import queue
import os
import time
from collections import Counter

def executar_processamento(pasta_entrada, pasta_saida, num_threads):
    fila_arquivos = queue.Queue()
    lock_contador = threading.Lock()
    arquivos_processados = [0]

    def processar_arquivo(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
        except FileNotFoundError:
            return

        palavras = texto.lower().split()
        contagem = Counter(palavras)

        nome_arquivo = os.path.basename(caminho_arquivo)
        caminho_saida = os.path.join(pasta_saida, nome_arquivo + ".out")
        os.makedirs(pasta_saida, exist_ok=True)

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            for palavra, quantidade in contagem.items():
                f.write(f"{palavra}: {quantidade}\n")

        with lock_contador:
            arquivos_processados[0] += 1

    def trabalhador():
        while True:
            try:
                caminho_arquivo = fila_arquivos.get(timeout=2)
                processar_arquivo(caminho_arquivo)
                fila_arquivos.task_done()
            except queue.Empty:
                break

    arquivos = [os.path.join(pasta_entrada, f) for f in os.listdir(pasta_entrada) if f.endswith('.txt')]
    for arq in arquivos:
        fila_arquivos.put(arq)

    inicio = time.time()

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=trabalhador)
        t.start()
        threads.append(t)

    fila_arquivos.join()
    for t in threads:
        t.join()

    fim = time.time()
    duracao = fim - inicio
    throughput = arquivos_processados[0] / duracao if duracao > 0 else 0

    return arquivos_processados[0], duracao, throughput
