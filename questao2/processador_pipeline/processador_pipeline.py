import threading
import queue
import os
import time

# Parâmetros de configuração
PASTA_ENTRADA = "entrada"
PASTA_SAIDA = "saida"
NUM_THREADS_LEITURA = 2
NUM_THREADS_PROCESSAMENTO = 2
NUM_THREADS_GRAVACAO = 2

# Filas entre os estágios
fila_leitura = queue.Queue()
fila_processamento = queue.Queue()
fila_saida = queue.Queue()

# Estágio 1: leitura dos arquivos
def leitor():
    while True:
        try:
            caminho_arquivo = fila_leitura.get(timeout=2)
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
            nome = os.path.basename(caminho_arquivo)
            fila_processamento.put((nome, texto))
            fila_leitura.task_done()
        except queue.Empty:
            break

# Estágio 2: normalização do texto
def processador():
    while True:
        try:
            nome, texto = fila_processamento.get(timeout=2)
            texto_normalizado = texto.lower()  # ou .upper()
            fila_saida.put((nome, texto_normalizado))
            fila_processamento.task_done()
        except queue.Empty:
            break

# Estágio 3: gravação em disco
def gravador():
    while True:
        try:
            nome, texto = fila_saida.get(timeout=2)
            os.makedirs(PASTA_SAIDA, exist_ok=True)
            with open(os.path.join(PASTA_SAIDA, nome + ".out"), 'w', encoding='utf-8') as f:
                f.write(texto)
            fila_saida.task_done()
        except queue.Empty:
            break

# Função principal
def main():
    arquivos = [os.path.join(PASTA_ENTRADA, f) for f in os.listdir(PASTA_ENTRADA) if f.endswith('.txt')]
    for arq in arquivos:
        fila_leitura.put(arq)

    inicio = time.time()

    # Criar e iniciar as threads dos três estágios
    leitores = [threading.Thread(target=leitor) for _ in range(NUM_THREADS_LEITURA)]
    processadores = [threading.Thread(target=processador) for _ in range(NUM_THREADS_PROCESSAMENTO)]
    gravadores = [threading.Thread(target=gravador) for _ in range(NUM_THREADS_GRAVACAO)]

    for t in leitores + processadores + gravadores:
        t.start()

    # Esperar o pipeline terminar
    fila_leitura.join()
    fila_processamento.join()
    fila_saida.join()

    for t in leitores + processadores + gravadores:
        t.join()

    fim = time.time()
    print(f"✅ Latência total: {fim - inicio:.2f} segundos")

if __name__ == "__main__":
    main()
