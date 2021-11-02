import socket
import argparse
import pickle
from enum import Enum

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
    parser.add_argument('-o',
                        '--operation',
                        type=str,
                        dest='operation',
                        help='Operacion a realizar',
                        required=True),
    parser.add_argument('-n',
                        '--first',
                        type=int,
                        dest='n',
                        help='Primer Operador',
                        required=True),
    parser.add_argument('-m',
                        '--second',
                        type=int,
                        dest='m',
                        help='Segundo operador',
                        required=True),
    
    args = parser.parse_args()
    print (args)
    if (args.operation != 'suma' and args.operation != 'resta' and args.operation != 'mult' and args.operation != 'div' and args.operation != 'pot'):
        print('Operadores deben ser suma, resta, mult, div, pot ')
        exit()
    SERVER_HOST = args.addr
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST,SERVER_PORT))
    msj = pickle.loads(s.recv(1024))
    print(msj)
    s.send(pickle.dumps([args.operation,args.n,args.m]))
    data = pickle.loads(s.recv(1024))
    print(f'Resultado: {data}')


