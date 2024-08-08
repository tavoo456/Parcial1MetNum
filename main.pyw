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
    
    def biseccion(self):       
        funcion = self.ui.txtFuncionMA.text()
        
        a = float(self.ui.txtA.text())        
        b = float(self.ui.txtB.text())
        
        tolerancia = int(self.ui.txtTolerancia.text())
        iMax = int(self.ui.txtNIteraciones.text())
        
        error = 100
        i = 1
        
        #-0.6*x**2 + 2.4*x + 5.5
        #"{0:.7f}".format(a)
        
        self.ui.twBiseccion.setRowCount(0)
        
        while error > tolerancia and i <= iMax: 
            m = (a+b)/2
            
            fa = eval(funcion, {"x": a})
            fb = eval(funcion, {"x": b})
            fm = eval(funcion, {"x": m})
            
            error = abs((b-a) / 2) * 100
            
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MetodosNumericos() 
    myapp.show()
    sys.exit(app.exec())