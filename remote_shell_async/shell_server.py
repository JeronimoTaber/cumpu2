'''
Reescriba el código del servidor remote_shell para que ahora, 
en vez de utilizar multiprocessing o threading para lograr atender a varios clientes simultáneamente, 
lo haga haciendo uso de concurrencia por medio de asyncio.
'''
import socket
import subprocess
import argparse
import shlex
import pickle
import asyncio

async def shell_hijo(cliente, addr)-> None:
    loop = asyncio.get_event_loop()
    print(f'cliente con addr: {addr}')

    while True:
        data = pickle.loads(await loop.sock_recv(cliente,1024))
        print(f'peticion con addr: {addr}')

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

        await loop.sock_sendall(cliente,pickle.dumps(msg))


    cliente.close()

async def main(args):
    SERVER_HOST = '127.0.0.1' 
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST,SERVER_PORT))
    s.listen(5)
    s.setblocking(False)

    loop = asyncio.get_event_loop()
    print(loop)

    while True:

        conn, addr = cliente, _= await loop.sock_accept(s)
        msg = 'conectado'
        conn.send(pickle.dumps(msg))
        print(f"Se realizo una nueva conneccion con: {addr}")
        loop.create_task(shell_hijo(cliente, addr))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remoe Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto Servidor',
                        required=True,type=int),
    
    args = parser.parse_args()
    print (args)
    asyncio.run(main(args))
    



