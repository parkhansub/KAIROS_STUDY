# from PyQt5.QtWidgets import *
# import sys
# import random


# class MainWindow(QMainWindow):

    


#     def __init__(self):
#         super().__init__()


#         button1 = QPushButton()
#         check = QCheckBox()
#         combo = QComboBox()
#         data = QDateEdit()
#         dial = QDial()
#         line = QLineEdit()
#         lcd = QLCDNumber()
#         pogress = QProgressBar()
#         slide = QSlider()
#         s = QScrollArea()
#         r = QRadioButton()


#         container = QWidget()
#         self.setCentralWidget(container)

#         h_layout = QVBoxLayout()
#         container.setLayout(h_layout)

#         h_layout.addWidget(button1)
#         h_layout.addWidget(check)
#         h_layout.addWidget(combo)
#         h_layout.addWidget(data)
#         h_layout.addWidget(dial)
#         h_layout.addWidget(line)
#         h_layout.addWidget(lcd)
#         h_layout.addWidget(pogress)
#         h_layout.addWidget(slide)
#         h_layout.addWidget(s)
#         h_layout.addWidget(r)
        
        

#         self.show()



# app = QApplication(sys.argv)
# win = MainWindow()
# app.exec()
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QDateEdit, QTimeEdit, 
                             QDoubleSpinBox, QComboBox, QSlider, QDial, QCheckBox, QLineEdit, QLabel, 
                             QColorDialog, QPushButton, QTextEdit, QProgressBar, QGraphicsScene, QGraphicsView)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 레이아웃 생성
        main_layout = QVBoxLayout()

        # 체크박스 추가
        self.checkbox = QCheckBox('Checkbox')
        self.checkbox.stateChanged.connect(self.update_progress)
        main_layout.addWidget(self.checkbox)

        # 콤보박스 추가
        self.combobox = QComboBox()
        self.combobox.addItems(["Option 1", "Option 2", "Option 3"])
        self.combobox.currentIndexChanged.connect(self.update_progress)
        main_layout.addWidget(self.create_labeled_widget('Combo Box:', self.combobox))

        # 날짜 편집기 추가
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.dateChanged.connect(self.update_progress)
        main_layout.addWidget(self.create_labeled_widget('Date Edit:', self.date_edit))

        # 시간 편집기 추가
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("AP hh:mm")
        self.time_edit.timeChanged.connect(self.update_progress)
        main_layout.addWidget(self.create_labeled_widget('Time Edit:', self.time_edit))

        # RGB 다이얼 추가
        self.dial_r = QDial()
        self.dial_r.setMaximum(255)
        self.dial_r.valueChanged.connect(self.update_color)
        self.dial_r_label = QLabel('R: 0')

        self.dial_g = QDial()
        self.dial_g.setMaximum(255)
        self.dial_g.valueChanged.connect(self.update_color)
        self.dial_g_label = QLabel('G: 0')

        self.dial_b = QDial()
        self.dial_b.setMaximum(255)
        self.dial_b.valueChanged.connect(self.update_color)
        self.dial_b_label = QLabel('B: 0')

        main_layout.addWidget(self.create_labeled_widget('Dial R:', self.dial_r, self.dial_r_label))
        main_layout.addWidget(self.create_labeled_widget('Dial G:', self.dial_g, self.dial_g_label))
        main_layout.addWidget(self.create_labeled_widget('Dial B:', self.dial_b, self.dial_b_label))

        # 더블 스핀박스 추가
        self.double_spin_box = QDoubleSpinBox()
        self.double_spin_box.valueChanged.connect(self.sync_slider_spinbox)
        main_layout.addWidget(self.create_labeled_widget('Double Spin Box:', self.double_spin_box))

        # 슬라이더 추가
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.sync_slider_spinbox)
        main_layout.addWidget(self.create_labeled_widget('Slider:', self.slider))

        # 라인 편집기 추가
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.update_final_label)
        main_layout.addWidget(self.create_labeled_widget('Line Edit:', self.line_edit))

        # 텍스트 편집기 추가
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.update_progress)
        main_layout.addWidget(self.create_labeled_widget('Text Edit:', self.text_edit))

        # 프로그레스 바 추가
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        main_layout.addWidget(self.progress_bar)

        # 최종 입력 값을 표시하는 라벨 추가
        self.final_label = QLabel('Final Value: ')
        main_layout.addWidget(self.final_label)

        self.setLayout(main_layout)
        self.setWindowTitle('Creative Widgets')

        # 프로그레스 바 업데이트 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start(100)

    def create_labeled_widget(self, label_text, widget, label_widget=None):
        """레이블과 위젯을 수평으로 배치"""
        layout = QHBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)
        layout.addWidget(widget)
        if label_widget:
            layout.addWidget(label_widget)
        container = QWidget()
        container.setLayout(layout)
        return container

    def sync_slider_spinbox(self, value):
        """슬라이더와 더블 스핀박스를 동기화"""
        if self.sender() == self.slider:
            self.double_spin_box.setValue(value)
        elif self.sender() == self.double_spin_box:
            self.slider.setValue(int(value))
        self.update_progress()

    def update_color(self):
        """RGB 값을 이용해 배경색 변경"""
        r = self.dial_r.value()
        g = self.dial_g.value()
        b = self.dial_b.value()
        self.dial_r_label.setText(f'R: {r}')
        self.dial_g_label.setText(f'G: {g}')
        self.dial_b_label.setText(f'B: {b}')
        color = QColor(r, g, b)
        self.setStyleSheet(f"background-color: {color.name()};")

    def update_final_label(self, text):
        """최종 입력 값을 업데이트"""
        self.final_label.setText(f'Final Value: {text}')
        self.update_progress()

    def update_progress(self):
        """입력 값에 따라 프로그레스 바 업데이트"""
        progress = 0
        if self.checkbox.isChecked():
            progress += 10
        if self.combobox.currentIndex() != -1:
            progress += 10
        if self.date_edit.date().isValid():
            progress += 10
        if self.time_edit.time().isValid():
            progress += 10
        if self.dial_r.value() != 0 or self.dial_g.value() != 0 or self.dial_b.value() != 0:
            progress += 10
        if self.double_spin_box.value() != 0.0:
            progress += 10
        if self.slider.value() != 0:
            progress += 10
        if self.line_edit.text() != "":
            progress += 10
        if self.text_edit.toPlainText() != "":
            progress += 10

        self.progress_bar.setValue(progress)

    def update_progress_bar(self):
        """타이머를 통해 프로그레스 바 애니메이션 효과 추가"""
        value = self.progress_bar.value()
        self.progress_bar.setValue((value + 1) % 101)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
