from PySide6.QtWidgets import *
from formulario import * 
from PySide6 import *
import sys

class MetodosNumericos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalcularBiseccion.clicked.connect(self.biseccion)
        self.ui.btnCalcularFalsaPosicion.clicked.connect(self.falsa_posicion)
        self.center()
        
    def center(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        size = self.geometry()
        
        x = (screen_rect.width() - size.width()) / 2
        y = (screen_rect.height() - size.height()) / 2
        
        self.move(x, y)
    
    def biseccion(self):
        #-0.6*x**2 + 2.4*x + 5.5       
        funcion = self.ui.txtFuncionMA.text()
        
        a = round(float(self.ui.txtA.text()), 7)
        b = round(float(self.ui.txtB.text()), 7)
        tolerancia = round(float(self.ui.txtTolerancia.text()), 7)
        
        iMax = int(self.ui.txtNIteraciones.text())

        error = 100
        i = 1
            
        self.ui.twBiseccion.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            m = (a + b) / 2

            fa = round(eval(funcion, {"x": a}), 7)
            fb = round(eval(funcion, {"x": b}), 7)
            fm = round(eval(funcion, {"x": m}), 7)

            error = round(abs((b - a) / 2) * 100, 7)
                        
            self.AñadirDatosBiseccion([i, a, b, m, fa, fb, fm, error])
            
            if fa * fm < 0:
                b = m
            else:
                a = m                      
            
            i += 1            

    def AñadirDatosBiseccion(self, datos):
        fila = self.ui.twBiseccion.rowCount()

        self.ui.twBiseccion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twBiseccion.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def falsa_posicion(self):
        funcion = self.ui.txtFuncionMA.text()
        
        a = round(float(self.ui.txtA.text()), 7)
        b = round(float(self.ui.txtB.text()), 7)
        tolerancia = round(float(self.ui.txtTolerancia.text()), 7)
        
        iMax = int(self.ui.txtNIteraciones.text())

        error = 100
        xrAnterior = 0
        i = 1                  
             
        self.ui.twFalsaPosicion.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            fa = round(eval(funcion, {"x": a}), 7)
            fb = round(eval(funcion, {"x": b}), 7)
            
            xr = round(b - (fb*(b - a))/(fb - fa), 7)       

            error = round(abs((xr - xrAnterior)/xr) * 100, 7)
            
            xrAnterior = xr
            
            fxr = round(eval(funcion, {"x": xr}), 7)
            
            self.AñadirDatosFalsaPosicion([i, a, b, xr, fa, fb, fxr, error])
            
            if fa * fxr < 0:
                b = xr
            else:
                a = xr                      
            
            i += 1
            
    def AñadirDatosFalsaPosicion(self, datos):
        fila = self.ui.twFalsaPosicion.rowCount()

        self.ui.twFalsaPosicion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twFalsaPosicion.setItem(fila, columna, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())