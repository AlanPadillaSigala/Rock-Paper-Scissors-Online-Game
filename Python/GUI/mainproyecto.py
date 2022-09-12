import sys
from confWidget import Ui_Form
from PySide2.QtWidgets import QApplication, QMainWindow ,QDialog ,QPushButton, QDialogButtonBox,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit

import socket
from threading import Thread 


class QtWindow(QMainWindow):

    s=socket.socket()
    server_host='18.211.34.177'
    server_port=3005
    
    seleccion = ''
    numGanadosL = 0
    numPerdidosL = 0
    numEmpatadosL = 0

    numGanadosT = 0
    numPerdidosT = 0
    numEmpatadosT = 0

    def __init__(self):
        super(QtWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
    def seleccionar(self):
        self.seleccion = self.ui.Seleccion.currentText()
        #print(self.seleccion)
        if self.seleccion == 'Piedra':
            self.s.send(b'1')   #Envio de respuesta
            self.ui.opcion.setText(self.seleccion)            

        elif self.seleccion == 'Papel':
            self.s.send(b'2')   #Envio de respuesta            
            self.ui.opcion.setText(self.seleccion)

        elif self.seleccion == 'Tijera':
           self.s.send(b'3')   #Envio de respuesta
           self.ui.opcion.setText(self.seleccion)            

        else:
            print('Opcion no valida')

    def cerrar (self):
       # self.mensajeJuego('Puedes Cerrar Ventana')
       # self.s.send(b'n')

        self.continueF1()

    def salioContrincante(self, respuesta):
        if respuesta == b'----Salio Jugador----':
            self.continueF2()
            
        elif respuesta == b'----no salio Jugador----':
            ...
            
    
    def numJugador(self, texto):
        self.ui.LJugador.setText(texto)
    
    def mensajeServidor(self, texto):
        self.ui.LMensajeServidor.setText(texto)

    def mensajeJuego(self, texto):
        self.ui.LMensajeJuego.setText(texto)

    def resJugador(self, texto):
        self.ui.LRespuestaJugador.setText(texto)

    def contadorLocal(self, respuesta):
        if respuesta == b'----GANASTE----':
            self.numGanadosL += 1
            self.ui.ganadosL.display(self.numGanadosL)
        elif respuesta == b'----PERDISTE----':
            self.numPerdidosL += 1
            self.ui.perdidosL.display(self.numPerdidosL)
        elif respuesta == b'----EMPATE----':
            self.numEmpatadosL += 1
            self.ui.empatadosL.display(self.numEmpatadosL)
        else:
            self.numGanadosL = 0
            self.numPerdidosL = 0
            self.numEmpatadosL = 0
            self.ui.ganadosL.display(self.numGanadosL)
            self.ui.perdidosL.display(self.numPerdidosL)
            self.ui.empatadosL.display(self.numEmpatadosL)

    def contadorTotal(self, respuesta):
        if respuesta == b'----GANASTE----':
            self.numGanadosT += 1
            self.ui.ganadosT.display(self.numGanadosT)
        elif respuesta == b'----PERDISTE----':
            self.numPerdidosT += 1
            self.ui.perdidosT.display(self.numPerdidosT)
        elif respuesta == b'----EMPATE----':
            self.numEmpatadosT += 1
            self.ui.empatadosT.display(self.numEmpatadosT)

    def msgContrincante(self, respuesta):
        opc = self.ui.opcion.text()
        # Ganaste
        if respuesta == '----GANASTE----' and opc == 'Piedra':
            self.mensajeJuego('Tijera')#imprime tijera
        elif respuesta == '----GANASTE----' and opc == 'Papel':
            self.mensajeJuego('Piedra')#imprime piedra
        elif respuesta == '----GANASTE----' and opc == 'Tijera':
            self.mensajeJuego('Papel')#imprime papel

        # Perdiste
        if respuesta == '----PERDISTE----' and opc == 'Piedra':
            self.mensajeJuego('Papel')#imprime papel
        elif respuesta == '----PERDISTE----' and opc == 'Papel':
            self.mensajeJuego('Tijera')#imprime tijera
        elif respuesta == '----PERDISTE----' and opc == 'Tijera':
            self.mensajeJuego('Piedra')#imprime piedra

        # Empate
        if respuesta == '----EMPATE----' and opc == 'Piedra':
            self.mensajeJuego('Piedra')#imprime piedra
        elif respuesta == '----EMPATE----' and opc == 'Papel':
            self.mensajeJuego('Papel')#imprime papel
        elif respuesta == '----EMPATE----' and opc == 'Tijera':
            self.mensajeJuego('Tijera')#imprime tijera  

    def juego(self, i):
        Grande = False
        salir = False
        salir2 = False
        escapa = False
        reiniciar = False
        condicion = ''

        try:
            self.s.connect((self.server_host,self.server_port))
        except ConnectionRefusedError:
            print('Servidor NO activo')
            msj = 'Servidor NO activo'
            self.mensajeServidor(msj)
            print('Saliendo...')
            sys.exit()

        while not Grande:
            print('Listo para recibir')
            Jugador = self.s.recv(1000)   #1 recibe numero jugador
            str_Jugador = Jugador.decode()
            self.numJugador(str_Jugador)
            print(Jugador)

            condicion=self.s.recv(1080)   #recibe condicion para inicar
            print(condicion)
            str_condicion = condicion.decode()
            self.mensajeServidor(str_condicion)

            while not salir:
                reiniciar = False
                if condicion == b'inicia':
            
                    EnviaRespuesta = False
                    while not salir2:
                        #self.mensajeJuego('Seleccione respuesta')

                        if not EnviaRespuesta:
                            self.ui.BJugar.clicked.connect(self.seleccionar)
                            self.ui.BCerrar.clicked.connect(self.cerrar)
                            EnviaRespuesta = True

                        respuesta=self.s.recv(1080)   #Recibe respuesta del Juego
                        print(respuesta)
                        str_respuesta = respuesta.decode()
                        self.resJugador(str_respuesta)

                        self.contadorLocal(respuesta)
                        self.contadorTotal(respuesta)
                        self.msgContrincante(str_respuesta)

                        # if respuesta == b'----Salio Jugador----':
                        #     reiniciar = True
                        #     break
        

                else:
                    ResEspera = self.s.recv(1080)
                    str_ResEspera = ResEspera.decode()
                    self.mensajeServidor(str_ResEspera)
                    print(ResEspera)
                    condicion = ResEspera



                if escapa == True or reiniciar == True:
                    break

            if escapa == True:
                break

        print('saliendo')
        self.s.close()

    def continueF1(self):
        if self.continueDialg1():
            self.s.send(b'Y')
            print("Desea seguir Jugando...")
        else:
            self.s.send(b'N')
            self.close()
            print("Desea Salir...")

    def continueDialg1(self):
        dlg = QDialog(parent=self)
        dlg.setWindowTitle("Sin oponente ")
        dlg.setMinimumSize(300,140)


        dlg.Btn_Continue = QPushButton(self.tr("&Continuar"))
        dlg.Btn_Continue.setDefault(True)

        dlg.Btn_Exit = QPushButton(self.tr("&Abandonar"))
        dlg.Btn_Exit.setCheckable(True)
        dlg.Btn_Exit.setAutoDefault(False)

        dlg.message = QLabel("¿Seguro que quieres salir? ")

        dlg.layout1 = QHBoxLayout()
        dlg.layout2 = QVBoxLayout()
        
        dlg.layout1.addWidget(dlg.Btn_Continue)
        dlg.layout1.addWidget(dlg.Btn_Exit)

        dlg.layout2.addWidget(dlg.message)
        dlg.layout2.addLayout(dlg.layout1)

        dlg.setLayout(dlg.layout2)
        dlg.Btn_Continue.clicked.connect(dlg.accept)
        dlg.Btn_Exit.clicked.connect(dlg.reject)

        return dlg.exec()

    def continueF2(self):
        if self.continueDialg2():
            self.s.send(b'Y')
            print("Desea seguir Jugando...")
        else:
            self.s.send(b'N')
            self.close()
            print("Desea Salir...")

    def continueDialg2(self):
        dlg = QDialog(parent=self)
        dlg.setWindowTitle("Sin oponente ")
        dlg.setMinimumSize(300,140)


        dlg.Btn_Continue = QPushButton(self.tr("&Continuar"))
        dlg.Btn_Continue.setDefault(True)

        dlg.Btn_Exit = QPushButton(self.tr("&Abandonar"))
        dlg.Btn_Exit.setCheckable(True)
        dlg.Btn_Exit.setAutoDefault(False)

        dlg.message = QLabel(" Tu contrincante ha avandonado ¿Deseas continuar? ")

        dlg.layout1 = QHBoxLayout()
        dlg.layout2 = QVBoxLayout()
        
        dlg.layout1.addWidget(dlg.Btn_Continue)
        dlg.layout1.addWidget(dlg.Btn_Exit)

        dlg.layout2.addWidget(dlg.message)
        dlg.layout2.addLayout(dlg.layout1)

        dlg.setLayout(dlg.layout2)
        dlg.Btn_Continue.clicked.connect(dlg.accept)
        dlg.Btn_Exit.clicked.connect(dlg.reject)


        return dlg.exec()



# # while True:
# #         Readble=tuple() 
# #         readble,writable,exceptional = select.select(inputs,outputs,inputs,0.1) #multiplexacion de lectura de clientes
        
#         for s in exceptional: ## busca errores de conexion 
#             if s==J1:
#                 J1.close()
#                 J2.send('n'.encode('utf-8'))
#                 if wantContinue(J2):
#                     redirectPlayer(J2)
#                     return
#                 else:
#                     J2.close()
#                     print("fin del juego")
#                     return
                
                    

#             if s==J2:
#                 J2.close()
#                 J1.send('n'.encode('utf-8'))
#                 if wantContinue(J1):
#                     redirectPlayer(J1)
#                     return
#                 else:
#                     J2.close()
#                     print("fin del juego")
#                     return  

#         for s in readble:
#             data=s.recv(20).decode('utf-8')
#             if data =="":
#                 continue

#             if data=='----Salio Jugador----':
#                 print("Alguien Abandono")

#                 if s==J1:
#                     # player1.close()
#                     player2.send('n'.encode('utf-8'))
#                     if wantContinue(J2):
#                         redirectPlayer(J2)
#                         return
#                     else:
#                         J2.close()
#                         print("fin del juego")
#                         return
                    
                        

#                 if s==player2:
#                     player2.close()
#                     player1.send('n'.encode('utf-8'))
#                     if wantContinue(player1):
#                         redirectPlayer(player1)
#                         return
#                     else:
#                         player2.close()
#                         print("fin del juego")
#                         return
                    
                
#                 break

app = QApplication()
window = QtWindow()
nueva = QtWindow()
#----Salio Jugador----
i=0
t = Thread(target=window.juego, args=(i ,))

window.show()

t.start()

sys.exit(app.exec_())
