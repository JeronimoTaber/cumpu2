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

def shell_hijo(cliente):
    conn, addr = cliente
    print(f'hijo cliente con addr: {addr}')

    while True:
        data = pickle.loads(conn.recv(1024))
        if data == 'quit':
            print('terminando hijo')
            break
        comands = shlex.split(data)
        print (comands)
        p = subprocess.Popen(comands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if(stdout):
            stdout=('ok\n'+stdout.decode())
            msg = stdout
        if(stderr):
            stderr=('Error\n'+stderr.decode())
            msg = stderr
        if(not stderr and not stdout):
            msg = ('El comando no devolvio error, pero no contiene una salida')

        print(msg)

        conn.send(pickle.dumps(msg))


    conn.close()
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remoe Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto Servidor',
                        required=True,type=int),
    
    args = parser.parse_args()
    print (args)
    SERVER_HOST = '127.0.0.1' 
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
        for thread in threading.enumerate(): 
            print(f'Thread activo: {thread.name}')


