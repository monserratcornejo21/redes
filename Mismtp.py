#importamos funciones socket
import socket

#establecemos una funcion para manejar la cantidad de bits que tendra el mensaje, transformacion de 16 a 8 y viceversa
def enviar(conexion,men):
    print(men)
    msg = men + '\n'
    conexion.send(msg.encode())

def recibir(conexion):
    msg = conexion.recv(1024)
    print(msg.decode())
#establecemos variables
def Mismtp(From,to,Subject,Message):
    host = '192.168.0.24'
    port = 25
    ipv4 = socket.AF_INET
    tcp  = socket.SOCK_STREAM
    user = input

    # con datos entregados por la estructura TCP y ipv4, a la direccion de coneccion le damos un orden de ejecucion segun datos ingresados por usuario 
    with socket.socket(ipv4,tcp) as conexion:

        conexion.connect((host, port))
        recibir(conexion)
        enviar(conexion,'HELO')
        recibir(conexion)
        enviar(conexion,'MAIL FROM: ',From)
        recibir(conexion)
        enviar(conexion,'RCPT TO: ',to)
        recibir(conexion)
        enviar(conexion,'DATA')
        recibir(conexion)
        enviar(conexion,'Subject: ',Subject)
        enviar(conexion,'From:'+From)
        enviar(conexion,'To: '+to)
        enviar(conexion,'')
        enviar(conexion,Message)
        enviar(conexion,'')
        enviar(conexion,'.')
        recibir(conexion)
        enviar(conexion,'quit')