from socket import socket
from threading import Thread
import time

cliente = []
respuesta = [0,0]
NumClient = 0
contadorBorraRes = 0
Grande = False

def clientes(sock, counter):
    while not Grande:
        #Numero de jugador
        msg = f'Jugador [{counter}]'
        sock.send(msg.encode())   # 1er envio: numero jugador
        print(msg)
        time.sleep(1)
        
        #lista de clientes
        cliente.append(counter)   #incrementa la lista cuando hay un nuevo cliente

        salirWhile = False
        salirWhile2 = False
        esperarCliente = False
        esperarRespuesta = False
        envia = False
        cliente1 = False
        cliente2 = False
        salioCliente1 = False
        salioCliente2 = False
        global contadorBorraRes  # Variables globales que se usan dentro de la funcion
        global respuesta         # '''                    '''                      '''

        while not salirWhile:
            if len(cliente) == 2:   #Entra solo si en la lista hay 2 elementos (2 Clientes)
                if not envia:
                    sock.send(b'inicia')    #Envia solo una ves el disparo para iniciar el juego en clientes
                    envia = True
    
                guardaRespuesta = sock.recv(1080)   #Recibe respuesta del cliente

                if counter == 1:    #----- Si cliente 1, entonces guarda en la posicion 0 de lista respuesta
                    respuesta[0] = guardaRespuesta
                elif counter == 2:  #----- Si cliente 2, entonces guarda en la posicion 0 de lista respuesta
                    respuesta[1] = guardaRespuesta
                print(respuesta)    # Muestra las respuestas en el servidor

                while not salirWhile2:  

                    # Entra solamente si cada cliente ingreso su respuesta (linea 38 a 41)
                    if respuesta != [0,0] and respuesta != [0,respuesta[1]] and respuesta != [respuesta[0],0]:
                        
                        if counter == 1:    
                            if not cliente1:   # if para ejecutar una sola vez (evita el reenvio de multiples respuestas)
                                
                                j1 = respuesta[0]
                                j2 = respuesta[1]

                                print(f'inicia juego [{counter}]')
                                print(F"{j1} VS {j2}") 

                                if j1==b'N' or j1 == b'n':
                                    print(f'salio: {addr}')
                                    sock.close()
                                    salioCliente1 = True
                                    salirWhile2 = True

    # ---------------------------------------------------------------------------------------------                                
                                elif j2 == b'N' :
                                    sock.send(b'----Salio Jugador----')
    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------                                
                                elif j2 == b'Y' :
                                    sock.send(b'----no salio Jugador----')
    # ---------------------------------------------------------------------------------------------
                                
                                elif j1==b'1'or j1== b'2'or j1==b'3':
                                    j1=int(j1)
                                    j2=int(j2)
                                    if j1==j2:
                                        sock.send(b'----EMPATE----')  #Envia respuesta de juego a cliente
                                    else:
                                        if j1==1:
                                            if j2== 2:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                        elif j1==2:
                                            if j2== 3:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                        else:
                                            if j2== 1:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                contadorBorraRes += 1   #Contador para borrar las respuestas y jugar de nuevo
                                cliente1 = True

                        if counter == 2:
                            if not cliente2:   # if para ejecutar una sola vez (evita el reenvio de multiples respuestas)

                                j1 = respuesta[1]
                                j2 = respuesta[0]

                                print(f'inicia juego [{counter}]')
                                print(F"{j1} VS {j2}") 
                                if j1==b'N' or j1 == b'n':
                                    print(f'salio: {addr}')
                                    sock.close()
                                    salioCliente2 = True
                                    salirWhile2 = True

    # ---------------------------------------------------------------------------------------------                                
                                elif j2 == b'N' :
                                    sock.send(b'----Salio Jugador----')
                                    salirWhile = True
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------                                
                                elif j2 == b'Y' :
                                    sock.send(b'----no salio Jugador----')
    # ---------------------------------------------------------------------------------------------

                                elif j1==b'1'or j1== b'2'or j1==b'3':
                                    j1=int(j1)
                                    j2=int(j2)
                                    if j1==j2:
                                        sock.send(b'----EMPATE----')  #Envia respuesta de juego a cliente
                                    else:
                                        if j1==1:
                                            if j2== 2:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                        elif j1==2:
                                            if j2== 3:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                        else:
                                            if j2== 1:
                                                sock.send(b'----PERDISTE----')  #Envia respuesta de juego a cliente
                                            else:
                                                sock.send(b'----GANASTE----')  #Envia respuesta de juego a cliente
                                contadorBorraRes += 1   #Contador para borrar las respuestas y jugar de nuevo  
                                cliente2 = True                   

                        if contadorBorraRes == 2:   #Contador para borrar las respuestas y jugar de nuevo
                            respuesta = [0,0]
                            contadorBorraRes = 0
                            cliente1 = False
                            cliente2 = False
                            break
                        if counter == 1 or counter == 2:   # if para regresar a todos los clientes y jugar de nuevo
                            cliente1 = False
                            cliente2 = False
                            break
                            
                            

                    else:
                        if not esperarRespuesta:
                            EsperaRespuesta = b'esperando respuesta del otro jugador'
                            #sock.send(EsperaRespuesta.encode())
                            print(EsperaRespuesta)
                            esperarRespuesta = True
                
                if salirWhile == True and counter == 2:
                    cliente.clear()
                    counter = 1
                    break

                elif salirWhile == True and counter == 1:
                    cliente.clear()
                    counter = 1
                    break

            else:
                if not esperarCliente:
                    EsperaJugador = b'Esperando contrincante'
                    sock.send(EsperaJugador)
                    print(EsperaJugador)
                    esperarCliente = True

    # ---------------------------------------------------------------------------------------------
            if salirWhile2 == True:
                break
        
        if salioCliente1 == True:
            break
        elif salioCliente2 == True:
            break
    # ---------------------------------------------------------------------------------------------
    print('-****- Esto solo se ve saliendo del while principal -****-')
    global NumClient
    NumClient = 0
    respuesta = [0,0]
    cliente.clear()  


s=socket()
host= '0.0.0.0'
port=3005

s.bind((host,port))

print("Esperando conexion...")
s.listen(2)

while True:
    conn,addr=s.accept()  #Acepta los clientes
    NumClient += 1  # Este es el contador de clientes
    print(f"Direccion: {addr}")

    if NumClient == 1 or NumClient == 2:
        #Define funcion para multiproceso
        t = Thread(target=clientes, args=(conn, NumClient))
        t.start() #Inicia para cada cliente
    else:
        conn.send(b'Servidor ocupado')


