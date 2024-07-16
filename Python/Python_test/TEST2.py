from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider
import sys
from PyQt5.QtCore import Qt

app = QApplication([])


class mainwindow(QMainWindow):
 
 def __init__(self):
    super().__init__()

    container = QWidget()
    v_layout = QVBoxLayout()
# 위젯 배치에 활용되는 코드 참조만 하세
    self.setCentralWidget(container)
 ##########.setLayout(v_layout)
    slider = QSlider()
    slider.setOrientation(Qt.Horizontal)
    v_layout.addWidget(slider)
####### label 추가


#슬라이드가 움직인 위치 값
    print(self.slider.value())


# 3개의 슬라이드 값을 저장하는 리스트 참조 (코드는 추가하셔야 합니다)
    self.sliders = []
    for i in range(3):
        self.slider = QSlider()
        self.slider.setRange(0, 180)              
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.valueChanged.connect(self.update_label)


win = mainwindow()
app.exec(sys.argv)