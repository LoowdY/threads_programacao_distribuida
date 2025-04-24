import socket
import time
import threading
from shared import enviar_json, receber_json, TIPO_BEAT, TIPO_READY, TIPO_PROCESS, TIPO_RESULT

HOST = 'localhost'
PORT = 5000

def enviar_beats_periodicamente(conn):
    while True:
        enviar_json(conn, {"tipo": TIPO_BEAT})
        time.sleep(5)

def iniciar_worker():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[✓] Worker conectado ao scheduler")

        threading.Thread(target=enviar_beats_periodicamente, args=(s,), daemon=True).start()

        while True:
            msg = receber_json(s)
            if msg and msg["tipo"] == TIPO_PROCESS:
                nome = msg["nome"]
                conteudo = msg["conteudo"]
                texto = conteudo.lower()  # simula etapa de processamento
                enviar_json(s, {
                    "tipo": TIPO_RESULT,
                    "nome": nome,
                    "resultado": texto
                })
                print(f"[⇄] {nome} processado e enviado")

if __name__ == "__main__":
    iniciar_worker()
