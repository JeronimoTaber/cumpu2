import socket
import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remoe Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto Servidor',
                        required=True,type=int),
    parser.add_argument('-t',
                        '--type',
                        type=str,
                        dest='type',
                        help='tcp o udp',
                        required=True),
    parser.add_argument('-a',
                        '--addr',
                        type=str,
                        dest='addr',
                        help='Direccion ip servidor',
                        required=True),
    
    args = parser.parse_args()
    print (args)
    SERVER_HOST = '127.0.0.1' 
    SERVER_PORT = args.port
    if (args.type == 'tcp'):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST,SERVER_PORT))

    elif (args.type == 'udp'):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        print(f'ERROR: {args.type} es un protocolo no valido')
        exit()
    data = ''
    for line in sys.stdin:
        data += line
    
    print(data)
    if(args.type == 'tcp'):
        s.sendall(data.encode())
        s.send('\nEOF'.encode())
    else:
        s.sendto(data.encode(),(SERVER_HOST,SERVER_PORT))
        s.sendto('EOF'.encode(),(SERVER_HOST,SERVER_PORT))


         
    # while True:
    #     print("CMD: ", end="")
    #     comando = input()

    #     if (comando == 'quit'):
    #         s.send(comando.encode('ascii'))
    #         break
        
    #     s.send(comando.encode('ascii'))
    #     data = s.recv(1024).decode()
    #     print(data)


