import socket
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remoe Shell Server - Tp3')
    parser.add_argument('-p',
                        '--port',
                        dest='port',
                        help='Puerto',
                        required=True,
                        type=int),
    parser.add_argument('-ho',
                        '--host',
                        type=str,
                        dest='host',
                        help='URL',
                        required=True),
    args = parser.parse_args()
    print (args)
    SERVER_HOST = args.host
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST,SERVER_PORT))
    '''
    hello|<nombre>
    email|<correo_electronico>
    key|<clave_hardodeada>
    exit
    '''

    stage = 0
    salir = False
    while True:
#        print("Recibido: %s" % msg)

        if stage == 0:
            print("nombre: ", end="")
            comando=input()
            comando = 'hello '+ comando

        elif stage == 1:
            print("email: ", end="")
            comando=input()
            comando = 'email '+ comando
        elif stage == 2:
            print("key: ", end="")
            comando=input()
            comando = 'key '+ comando    
        else:
            print("exit")
            comando = 'exit '
            salir=True

        s.send(comando.encode('ascii'))
        data = s.recv(512).decode()
        if data == '200':
            if (salir == True):
                exit()
            stage += 1
        else:
            print('error')
        print(data)


