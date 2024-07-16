from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QSlider, QLabel, QApplication, QMainWindow, QWidget
import sys

class MainWindow(QMainWindow):

    def __init__(self) :
        super().__init__()

        self.setWindowTitle("Arm Control")

        container = QWidget()
        self.setCentralWidget(container)

        h_layout = QVBoxLayout()
        container.setLayout(h_layout)

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(1,180)
        self.slider1.setValue(90)
        self.slider1.valueChanged.connect(self.update_label)
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(1,180)
        self.slider2.setValue(90)
        self.slider2.valueChanged.connect(self.update_label)
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setRange(1,180)
        self.slider3.setValue(90)
        self.slider3.valueChanged.connect(self.update_label)
    
    



        self.Label1 = QLabel("0")
        self.Label2 = QLabel("0")
        self.Label3 = QLabel("0")
        

        h_layout.addWidget(self.Label1)
        h_layout.addWidget(self.slider1)
        h_layout.addWidget(self.Label2)
        h_layout.addWidget(self.slider2)
        h_layout.addWidget(self.Label3)
        h_layout.addWidget(self.slider3)
        


        



        self.show()

    def update_label(self):
            self.Label1.setText(str(self.slider1.value()))
            self.Label2.setText(str(self.slider2.value()))
            self.Label3.setText(str(self.slider3.value()))




app = QApplication(sys.argv)
win = MainWindow()
app.exec()

