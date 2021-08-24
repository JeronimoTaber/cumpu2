import socket
import argparse


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
    s.connect((SERVER_HOST,SERVER_PORT))
    msj = s.recv(1024).decode()
    print(msj)
    if(msj != 'conectado'):
        print('salir')
    while True:
        print("CMD: ", end="")
        comando = input()

        if (comando == 'quit'):
            s.send(comando.encode('ascii'))
            break
        
        s.send(comando.encode('ascii'))
        data = s.recv(1024).decode()
        print(data)


