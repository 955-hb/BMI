import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('BMI - Calculator')

        self.ui.result.hide()
        self.ui.result_label.hide()

        # calculate-Button aktivieren
        self.ui.calculateBTN.clicked.connect(self.calculate_bmi)

        # close-Button aktivieren
        self.ui.closeBTN.clicked.connect(self.close_programm)

    def calculate_bmi(self):
        groesse = self.ui.groesse.value()
        gewicht = self.ui.gewicht.value()

        if groesse !=0:
            self.ui.result.show()
            self.ui.result_label.show()
            bmi = round(gewicht / (groesse ** 2), 2)
            self.ui.result.setText(str(bmi))
        else:
            self.ui.result.setText('')


    def close_programm(self):
        self.close()


window = MainWindow()
window.show()
#Starten der Anwendungsschleife und Beenden der Anwendung
sys.exit(app.exec_())
