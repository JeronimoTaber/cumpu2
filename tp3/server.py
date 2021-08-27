
import socket
import argparse

def tcp_server(args):
    alldata = ""
    data=''
    SERVER_HOST = '' 
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST,SERVER_PORT))
    s.listen(1)
    conn, addr  = s.accept()
    while True:
        data = conn.recv(1024).decode()
        if (data[len(data) - 3 :]=='EOF'):
            alldata = alldata + data[:len(data) - 3 ]                 
            conn.close()
            break
        else:
            alldata = alldata + data   
    return alldata     

def udp_server(args):
    alldata = ""
    data=''
    SERVER_HOST = '' 
    SERVER_PORT = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST,SERVER_PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if(data.decode()=='EOF'):
            break
        alldata = alldata + data.decode()
    return alldata     

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
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        dest='file',
                        help='Ruta a un archivo de texto',
                        required=True),
    
    args = parser.parse_args()
    print (args)

    if (args.type == 'tcp'):
        alldata = tcp_server(args)
    elif (args.type == 'udp'):
        alldata = udp_server(args)
    else:
        print(f'ERROR: {args.type} es un protocolo no valido')
        exit()
        
    f = open(args.file, "w")
    f.write(alldata)
    f.close()


            

