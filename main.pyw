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
        self.ui.btnCalcularSecante.clicked.connect(self.secante)
        self.ui.btnCalcularSecanteModificada.clicked.connect(self.secante_modificada)
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
        #Función: -0.6*x**2 + 2.4*x + 5.5  
        #Rango: [A=5, B=10]
        funcion = self.ui.txtFuncionMC.text()
        
        a = self.ui.txtA.text()
        b = self.ui.txtB.text()
        tolerancia = self.ui.txtToleranciaMC.text()
        
        iMax = self.ui.txtNIteracionesMC.text()
        error = 100
        i = 1
        
        if funcion == "" or a == "" or b == "" or tolerancia == "" or iMax == "":
            self.ui.lblAvisosMC.setText("Avisos: \nIngrese los datos correctamente.")
        else:
            a = round(float(a), 7)
            b = round(float(b), 7)
            tolerancia = round(float(tolerancia), 7)        
            iMax = int(iMax)
            
            self.ui.twBiseccion.setRowCount(0)
        
            while error > tolerancia and i <= iMax:
                m = round((a + b) / 2, 7)

                fa = round(eval(funcion, {"x": a}), 7)
                fb = round(eval(funcion, {"x": b}), 7)
                fm = round(eval(funcion, {"x": m}), 7)

                error = round(abs((b - a) / 2) * 100, 7)
            
                self.añadir_datos_biseccion([i, a, b, m, fa, fb, fm, str(error) + " %"])
            
                if fa * fm < 0:
                    b = m
                else:
                    a = m                      

                if error<tolerancia or iMax == i:
                    self.ui.lblAvisosMC.setText("Resultados: \nIteración final: " + str(iMax) + "\nError alcanzado: " + str(error) + " %\nRaíz: " + str(m))
                
                i += 1     

    def añadir_datos_biseccion(self, datos):
        fila = self.ui.twBiseccion.rowCount()

        self.ui.twBiseccion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twBiseccion.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def falsa_posicion(self):
        #Función: -0.5*x**2 + 2.5*x + 4.5  
        #Rango: [A=0, B=7]        
        funcion = self.ui.txtFuncionMC.text()
        
        a = self.ui.txtA.text()
        b = self.ui.txtB.text()
        tolerancia = self.ui.txtToleranciaMC.text()
        
        iMax = self.ui.txtNIteracionesMC.text()
        error = 100
        xrAnterior = 0
        i = 1 
        
        if funcion == "" or a == "" or b == "" or tolerancia == "" or iMax == "":
            self.ui.lblAvisosMC.setText("Avisos: \nIngrese los datos correctamente.")
        else:
            a = round(float(a), 7)
            b = round(float(b), 7)
            tolerancia = round(float(tolerancia), 7)        
            iMax = int(iMax)
            
            self.ui.twFalsaPosicion.setRowCount(0)
            
            while error > tolerancia and i <= iMax: 
                fa = round(eval(funcion, {"x": a}), 7)
                fb = round(eval(funcion, {"x": b}), 7)

                xr = round(b - (fb*(b - a))/(fb - fa), 7)       
                error = round(abs((xr - xrAnterior)/xr) * 100, 7)

                xrAnterior = xr

                fxr = round(eval(funcion, {"x": xr}), 7)

                self.añadir_datos_falsa_posicion([i, a, b, xr, fa, fb, fxr, str(error) + " %"])

                if fa * fxr < 0:
                    b = xr
                else:
                    a = xr                      

                if error<tolerancia or iMax == i:
                    self.ui.lblAvisosMC.setText("Resultados: \nIteración final: " + str(iMax) + "\nError alcanzado: " + str(error) + " %\nRaíz: " + str(xr))
                
                i += 1
            
    def añadir_datos_falsa_posicion(self, datos):
        fila = self.ui.twFalsaPosicion.rowCount()

        self.ui.twFalsaPosicion.insertRow(fila)

        for columna, value in enumerate(datos):
            self.ui.twFalsaPosicion.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def punto_fijo(self):
        #Función original: x**2 + 2x - 7
        #Función despejada: 7/(x + 2)
        #Aproximación inical: 0
        funcion = self.ui.txtFuncionMA.text()
            
        Xo = round(float(self.ui.txtAproximacionInicial.text()), 7)        
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMA.text())

        Xi = 0
        error = 100
        i = 1
        
        self.ui.twPuntoFijo.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            Xi = round(eval(funcion, {"x": Xo}), 7)
            
            error = round(abs(((Xi - Xo)/Xi)*100), 7)
            
            self.añadir_datos_punto_fijo([i, Xo, Xi, error])
            
            Xo = Xi
                        
            i += 1
    
    def añadir_datos_punto_fijo(self, datos):
        fila = self.ui.twPuntoFijo.rowCount()
        
        self.ui.twPuntoFijo.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twPuntoFijo.setItem(fila, columna, QTableWidgetItem(str(value)))       
        
    def newton_raphson(self):
        #Función: x**5 + 3*x**2 + x
        #Aproximación inicial: -2
        funcion = self.ui.txtFuncionMA.text()      
        xo = round(float(self.ui.txtAproximacionInicial.text()), 7)
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)       
        iMax = int(self.ui.txtNIteracionesMA.text())
        error = 100
        xAnterior = 0.0
        i = 1
        
        self.ui.twNewtonRaphson.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            resultado = round(eval(funcion, {"x": xo}), 7)
            #x = sympy.symbols('x', real=True) # define la variable simbólica x
            #diff sirve para sacar la derivada
            derivada = sympy.diff(funcion,"x")
            resultado_der = round(eval(str(derivada), {"x": xo}),7)
            xr = round(xo - (resultado/resultado_der),7)      
            
            error = round(abs((xr - xo)/xr) * 100,7)
            #error = abs((xActual - xAnterior)/xActual) * 100
            self.añadir_datos_newton_raphson([i, xo, xr, error])
            xo = xr      
            i += 1
    
    def añadir_datos_newton_raphson(self, datos):
        fila = self.ui.twNewtonRaphson.rowCount()
        
        self.ui.twNewtonRaphson.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twNewtonRaphson.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def secante(self):
        #Función: 0.5*x**3 - 2*x**2 + 1
        #Xi-1=0 y Xi=1
        funcion = self.ui.txtFuncionMA.text()
            
        Xi = round(float(self.ui.txtAproximacionInicial.text()), 7)
        #X_i = Xi-1
        X_i = round(float(self.ui.txtXi_1.text()), 7)    
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMA.text())

        #X__i = Xi+1
        X__i = 0
        error = 100
        i = 1
        
        self.ui.twSecante.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            fxi = round(eval(funcion, {"x": Xi}), 7)
            fx_i = round(eval(funcion, {"x": X_i}), 7)
            
            X__i = round(Xi - (fxi*(X_i-Xi))/(fx_i-fxi), 7)
            
            error = round((abs((X__i-Xi)/X__i))*100, 7)
            
            self.añadir_datos_secante([i, X_i, Xi, fx_i, fxi, X__i, error])
            
            X_i = Xi
            Xi = X__i
                
            i += 1

    def añadir_datos_secante(self, datos):
        fila = self.ui.twSecante.rowCount()
        
        self.ui.twSecante.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twSecante.setItem(fila, columna, QTableWidgetItem(str(value)))
            
    def secante_modificada(self):
        #Función: x**2 - 2
        #Xi = 1 y dxi = 0.01
        funcion = self.ui.txtFuncionMA.text()
            
        Xi = round(float(self.ui.txtAproximacionInicial.text()), 7)
        dxi = round(float(self.ui.txtdxi.text()), 7)    
        tolerancia = round(float(self.ui.txtToleranciaMA.text()), 7)
        
        iMax = int(self.ui.txtNIteracionesMA.text())
        
        
        error = 100
        i = 1
        
        self.ui.twSecanteModificada.setRowCount(0)
        
        while error > tolerancia and i <= iMax:
            x_d = round(Xi + dxi, 7)
            fxi = round(eval(funcion, {"x": Xi}), 7)
            fx_d = round(eval(funcion, {"x": x_d}), 7)
            
            #X__1 = X+1
            X__i = round(Xi - ((dxi*fxi)/(fx_d - fxi)), 7)
            
            error = round((abs((X__i - Xi)/X__i))*100, 7)
            
            self.añadir_datos_secante_modifica([i, Xi, dxi, x_d, fxi, fx_d, X__i, error])
            
            Xi = X__i
                
            i += 1

    def añadir_datos_secante_modifica(self, datos):
        fila = self.ui.twSecanteModificada.rowCount()
        
        self.ui.twSecanteModificada.insertRow(fila)
        
        for columna, value in enumerate(datos):
            self.ui.twSecanteModificada.setItem(fila, columna, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())