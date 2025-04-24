import json

# Tipos de mensagens possíveis
TIPO_BEAT = "BEAT"
TIPO_READY = "READY"
TIPO_PROCESS = "PROCESS"
TIPO_RESULT = "RESULT"

# Envia mensagem via socket (objeto JSON)
def enviar_json(conn, data):
    msg = json.dumps(data).encode()
    conn.sendall(msg)

# Recebe mensagem JSON via socket
def receber_json(conn):
    data = conn.recv(4096)
    if not data:
        return None
    return json.loads(data.decode())
