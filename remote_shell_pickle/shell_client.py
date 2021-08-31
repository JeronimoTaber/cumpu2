import socket
import argparse
import pickle

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
    msj = pickle.loads(s.recv(1024))
    print(msj)
    if(msj != 'conectado'):
        print('salir')
    while True:
        print("CMD: ", end="")
        comando = input()
        s.send(pickle.dumps(comando))
        if (comando == 'quit'):
            break
        
        data = pickle.loads(s.recv(1024))
        print(data)


