from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider
import sys
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Robot Arm Controller")
        
        container = QWidget()
        self.setCentralWidget(container)
        v_layout = QVBoxLayout()
        container.setLayout(v_layout)

        self.sliders = []
        
        for i in range(3):
            slider = QSlider()
            slider.setRange(0, 180)
            slider.setValue(90)
            slider.setOrientation(Qt.Horizontal)
            slider.valueChanged.connect(self.update_label)
            self.sliders.append(slider)
            v_layout.addWidget(slider)
        
        self.label = QLabel('Slider1: 90, Slider2: 90, Slider3: 90', self)
        self.label.resize(400, 20)
        v_layout.addWidget(self.label)

        self.show()
        
    def update_label(self):
        values = [slider.value() for slider in self.sliders]
        self.label.setText(f'Slider1: {values[0]}, Slider2: {values[1]}, Slider3: {values[2]}')

app = QApplication(sys.argv)
win = MainWindow()
app.exec()





















