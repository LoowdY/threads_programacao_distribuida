import socket
import threading
import os
import queue
from shared import enviar_json, receber_json, TIPO_PROCESS, TIPO_RESULT

HOST = 'localhost'
PORT = 5000

nodos_idle = []
nodos_busy = {}
tarefas = queue.Queue()

def tratar_nodo(conn, addr):
    global nodos_idle, nodos_busy

    id_nodo = f"{addr[0]}:{addr[1]}"
    print(f"[+] Conectado: {id_nodo}")
    nodos_idle.append(conn)

    while True:
        try:
            msg = receber_json(conn)
            if msg is None:
                break
            if msg["tipo"] == TIPO_RESULT:
                nome = msg["nome"]
                resultado = msg["resultado"]
                with open(f"resultados/{nome}.out", 'w', encoding='utf-8') as f:
                    f.write(resultado)
                print(f"[✓] Resultado recebido de {id_nodo}: {nome}")
                nodos_busy.pop(conn)
                nodos_idle.append(conn)
        except:
            break

    if conn in nodos_idle:
        nodos_idle.remove(conn)
    elif conn in nodos_busy:
        nodos_busy.pop(conn)

    conn.close()
    print(f"[x] Desconectado: {id_nodo}")

def despachar_tarefas():
    while True:
        if not tarefas.empty() and nodos_idle:
            arquivo = tarefas.get()
            conn = nodos_idle.pop(0)
            nodos_busy[conn] = arquivo
            with open(f"entrada/{arquivo}", 'r', encoding='utf-8') as f:
                conteudo = f.read()
            enviar_json(conn, {
                "tipo": TIPO_PROCESS,
                "nome": arquivo,
                "conteudo": conteudo
            })
            print(f"[→] Tarefa enviada: {arquivo}")

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[⏳] Scheduler escutando em {HOST}:{PORT}")

        threading.Thread(target=despachar_tarefas, daemon=True).start()

        while True:
            conn, addr = s.accept()
            threading.Thread(target=tratar_nodo, args=(conn, addr), daemon=True).start()

def adicionar_tarefas():
    arquivos = [f for f in os.listdir("entrada") if f.endswith(".txt")]
    for arq in arquivos:
        tarefas.put(arq)
        print(f"[+] Tarefa adicionada: {arq}")

if __name__ == "__main__":
    os.makedirs("entrada", exist_ok=True)
    os.makedirs("resultados", exist_ok=True)
    adicionar_tarefas()
    servidor()
