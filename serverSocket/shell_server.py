'''
Reescribir el ejercicio de remote_shell_multicli para que el envío de texto por el socket viaje en formato serializado de pickle.

Además, si es el caso, evitar la generación de procesos zombies.

Para la entrega pegue en el campo de texto el enlace al commit final en su repositorio GIT.
'''
import subprocess
import argparse
import shlex
import pickle
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('handle')
        self.request.send(pickle.dumps('conectado'))
        while True:
            data = pickle.loads(self.request.recv(1024))
            if data == 'quit':
                print('terminando hijo')
                break
            else:
                print(data)
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
            self.request.send(pickle.dumps(msg))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remote Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto Servidor',
                        required=True,type=int),
    parser.add_argument('-m',
                        '--mode',
                        type=str,
                        dest='mode',
                        help='t for thread o f for fork',
                        required=True),
    
    
    args = parser.parse_args()
    print (args)

    SERVER_HOST = '0' 
    SERVER_PORT = args.port
    socketserver.TCPServer((SERVER_HOST,SERVER_PORT),MyTCPHandler)

    if (args.mode == 't'):
        with ThreadedTCPServer((SERVER_HOST,SERVER_PORT),MyTCPHandler) as server:
            server.serve_forever()
    elif (args.mode == 'f'):
        with ForkedTCPServer((SERVER_HOST,SERVER_PORT),MyTCPHandler) as server:
                server.serve_forever()
    else:
        print(f'ERROR: {args.mode} es un modo no valido')
        exit()




