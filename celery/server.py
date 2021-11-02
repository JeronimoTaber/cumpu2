'''
Reescribir el ejercicio de remote_shell_multicli para que el envío de texto por el socket viaje en formato serializado de pickle.

Además, si es el caso, evitar la generación de procesos zombies.

Para la entrega pegue en el campo de texto el enlace al commit final en su repositorio GIT.
'''
import socket
import subprocess
import argparse
import shlex
import threading
import pickle
from tasks import *

def shell_hijo(cliente):
    conn, addr = cliente
    print(f'hijo cliente con addr: {addr}')

    data = pickle.loads(conn.recv(1024))
    print (f"Operador: {data[0]}, Operando 1: {data[1]}, Operando 2: {data[2]}")
    operator = data[0]
    n = data[1]
    m = data[2]
    if(operator == 'suma'):
        res = suma.delay(n, m)
    elif(operator == 'resta'):
        res = resta.delay(n, m)
    elif(operator == 'mult'):
        res = mult.delay(n, m)
    elif(operator == 'pot'):
        res = pot.delay(n, m)
    elif(operator == 'div'):
        res = div.delay(n, m)

    response = (res.get(timeout=10))
    print(f"Respuesta: {response}")
    conn.send(pickle.dumps(response))
    conn.close()


    conn.close()
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remoe Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto Servidor',
                        required=True,type=int),
    parser.add_argument('-a',
                        '--addr',
                        type=str,
                        dest='addr',
                        help='Direccion ip servidor',
                        required=True),
    
    args = parser.parse_args()
    print (args)
    SERVER_HOST = args.addr
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST,SERVER_PORT))
    s.listen(5)

    while True:
        conn, addr = cliente = s.accept()
        msg = 'conectado'
        conn.send(pickle.dumps(msg))
        print(f"Se realizo una nueva conneccion con: {addr}")
        th = threading.Thread(target=shell_hijo, args=(cliente,))
        th.start()



