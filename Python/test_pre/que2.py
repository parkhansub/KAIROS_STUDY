import numpy as np
import random
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout

class MainWindow(QMainWindow):

    

    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("야구게임")

        container = QWidget()
        self.setCentralWidget(container)
        v_layout = QVBoxLayout()
        container.setLayout(v_layout)


        container.setLayout(v_layout)


        for i in range(10):
            num = i
            i = QPushButton(str(i))
            i.setFixedSize(70,70)
            i.clicked.connect(self.num_choice)
            v_layout.addWidget(i)
        
       
            

        
        self.show()

    def num_choice(self):
        print()



        


app = QApplication(sys.argv)
win = MainWindow()
app.exec()








