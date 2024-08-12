from PySide6.QtWidgets import *
from formulario import * 
from PySide6 import *
import sys
import sympy 

class MetodosNumericos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalcularBiseccion.clicked.connect(self.biseccion)
        self.ui.btnCalcularFalsaPosicion.clicked.connect(self.falsa_posicion)
        self.ui.btnCalcularPuntoFijo.clicked.connect(self.punto_fijo)
        self.ui.btnCalcularNewtonRaphson.clicked.connect(self.newton_raphson)
        self.center()
    
    #Esta función centra el form en la pantalla
    def center(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        size = self.geometry()
        
        x = (screen_rect.width() - size.width()) / 2
        y = (screen_rect.height() - size.height()) / 2
        
        self.move(x, y)
    
    def biseccion(self):
        #-0.6*x**2 + 2.4*x + 5.5       
        funcion = self.ui.txtFuncionMC.text()
        
        a = round(float(self.ui.txtA.text()), 7)
        b = round(float(self.ui.txtB.text()), 7)
        tolerancia = round(float(self.ui.txtToleranciaMC.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMC.text())
        error = 100
        i = 1
        
        self.ui.twBiseccion.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            m = round((a + b) / 2, 7)

            fa = round(eval(funcion, {"x": a}), 7)
            fb = round(eval(funcion, {"x": b}), 7)
            fm = round(eval(funcion, {"x": m}), 7)

            error = round(abs((b - a) / 2) * 100, 7)
            
            self.añadir_datos_biseccion([i, a, b, m, fa, fb, fm, error])
            
            if fa * fm < 0:
                b = m
            else:
                a = m                      
            
            i += 1            

    def añadir_datos_biseccion(self, datos):
        fila = self.ui.twBiseccion.rowCount()

        self.ui.twBiseccion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twBiseccion.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def falsa_posicion(self):
        funcion = self.ui.txtFuncionMC.text()
        
        a = round(float(self.ui.txtA.text()), 7)
        b = round(float(self.ui.txtB.text()), 7)
        tolerancia = round(float(self.ui.txtToleranciaMC.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMC.text())
        
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
            
            self.añadir_datos_falsa_posicion([i, a, b, xr, fa, fb, fxr, error])
            
            if fa * fxr < 0:
                b = xr
            else:
                a = xr                      
            
            i += 1
            
    def añadir_datos_falsa_posicion(self, datos):
        fila = self.ui.twFalsaPosicion.rowCount()

        self.ui.twFalsaPosicion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twFalsaPosicion.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def punto_fijo(self):
        funcion = self.ui.txtFuncionMA.text()
        funcion = funcion + " + x"
        
        xActual = round(float(self.ui.txtAproximacionInicial.text()), 7)
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMA.text())

        error = 100
        xAnterior = 0.0
        i = 1
        
        while error > tolerancia and i <= iMax: 
            resultado = round(eval(funcion, {"x": xActual}), 7)
            xActual = resultado
            
            error = abs((xActual - xAnterior)/xActual) * 100
            
            self.añadir_datos_punto_fijo([i, xActual, xAnterior, error])
            xAnterior = xActual
                        
            i += 1
    
    def añadir_datos_punto_fijo(self, datos):
        fila = self.ui.twPuntoFijo.rowCount()
        
        self.ui.twPuntoFijo.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twPuntoFijo.setItem(fila, columna, QTableWidgetItem(str(value)))       
        
    def newton_raphson(self):
        #x**5 + 3*x**2 + x
        funcion = self.ui.txtFuncionMA.text()      
        xo = round(float(self.ui.txtAproximacionInicial.text()), 7)
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)       
        iMax = int(self.ui.txtNIteracionesMA.text())
        error = 100
        xAnterior = 0.0
        i = 1
        while error > tolerancia and i <= iMax: 
            resultado = round(eval(funcion, {"x": xo}), 7)
            #x = sympy.symbols('x', real=True) # define la variable simbólica x
            #diff sirve para sacar la derivada
            derivada = sympy.diff(funcion,"x")
            resultado_der = round(eval(str(derivada), {"x": xo}),7)
            xr = round(xo - (resultado/resultado_der),7)      
            
            error = round(abs((xr - xo)/xr) * 100,7)
            #error = abs((xActual - xAnterior)/xActual) * 100
            self.añadir_datos_newton_raphson([i, xr, xo, error])
            xo = xr      
            i += 1
    
    def añadir_datos_newton_raphson(self, datos):
        fila = self.ui.twNewtonRaphson.rowCount()
        
        self.ui.twNewtonRaphson.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twNewtonRaphson.setItem(fila, columna, QTableWidgetItem(str(value)))  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())