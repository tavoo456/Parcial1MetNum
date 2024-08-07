from PySide6.QtWidgets import *
import sys
from formulario import * 
from PySide6 import *

class CLASEPRINCIPAL (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnCalcular.clicked.connect(self.BISECCION)
    
    def BISECCION(self):
        #Obtenemos los valores
        a = float(self.ui.txtA.text())
        b = float(self.ui.txtB.text())
        tolerancia = int(self.ui.txtTolerancia.text())
        funcion = self.ui.txtFuncion.text()
        imax = int(self.ui.txtIteracion.text())
        e = tolerancia + 1
        i = 1
        
        #-0.6*x**2 + 2.4*x + 5.5
        #"{0:.7f}".format(a)
        while e > tolerancia and i < imax: 
            m = (a+b)/2
            #Evaluamos la funcion 
            fa = eval(funcion, {"x": a})
            fb = eval(funcion, {"x": b})
            fm = eval(funcion, {"x": m})
            print("fa:", fa,"fb:", fb,"fm:", fm)
            e = abs((b-a) / 2) * 100
            if fa * fm < 0:
                b = m
            else:
                a = m
            print("e",e)
            print("a:", a,"b:", b,"m:", m)
            i += 1
        
        self.ui.txtAFinal.setText(str("{0:.7f}".format(a)))
        self.ui.txtBFinal.setText(str("{0:.7f}".format(b)))
        self.ui.txtRaiz.setText(str("{0:.7f}".format(m)))
        self.ui.txtError.setText(str("{0:.7f}".format(e)))
        self.ui.txtIteracionFinal.setText(str(i))
        #suma = float(self.ui.txtNumero1.text()) + float(self.ui.txtNumero2.text())    
        #self.ui.txtResultado.setText(str(suma))}

if __name__ == "__main__":
    app=QApplication(sys.argv)
    myapp=CLASEPRINCIPAL() 
    myapp.show()
    sys.exit(app.exec())