from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
import random







class MainWindow(QMainWindow):

    


    def __init__(self):
        super().__init__()

        self.candidates =["김무현", "김동희", "조권희", "김민우", "심승환", "심승환"]
        self.cho_pre = "박재준"
        self.cho_un = "박재준"

        self.setWindowTitle("Kairos")

        self.button_state1 = False
        self.button_state2 = False
        self.button1 = QPushButton("대표님")
        self.button2 = QPushButton("부대표님")
        self.button1.setStyleSheet("background-color: blue;")
        self.button2.setStyleSheet("background-color: blue;")
        self.button1.clicked.connect(self.click_button1)
        self.button2.clicked.connect(self.click_button2)
    
        


        container = QWidget()
        self.setCentralWidget(container)

        h_layout = QVBoxLayout()
        container.setLayout(h_layout)

        h_layout.addWidget(self.button1)
        h_layout.addWidget(self.button2)

        

        self.show()

    def click_button1(self):

        if self.button_state1 :
            self.button_state1 = not self.button_state1
            self.cho_pre = random.choice(self.candidates)

            while True:

                if self.cho_pre == self.cho_un:
                    self.cho_pre = random.choice(self.candidates)
                
                else:

                    # self.button1.setStyleSheet("background-color: blue;")
                    print(f"{self.cho_pre}님이 대표로 선정되었습니다.")
                    break
            
        
        else : 
            self.button_state1 = not self.button_state1
            # self.button1.setStyleSheet("background-color: red;")
            print(f"권한이 해지되었습니다.")
    

    def click_button2(self):

        if self.button_state2 :

            self.button_state2 = not self.button_state2
            self.cho_un = random.choice(self.candidates)

            while True:

                if self.cho_pre == self.cho_un:
                    self.cho_pre = random.choice(self.candidates)
                
                else:

                    # self.button2.setStyleSheet("background-color: blue;")
                    print(f"{self.cho_un}님이 부대표로 선정되었습니다.")
                    break
            
            
        
        else : 
            self.button_state2 = not self.button_state2
            # self.button2.setStyleSheet("background-color: red;")
            print(f"권한이 해지되었습니다.")



   

    



app = QApplication(sys.argv)
win = MainWindow()
app.exec()
