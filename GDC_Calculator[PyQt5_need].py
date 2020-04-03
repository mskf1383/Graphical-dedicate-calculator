"""by MSKF"""


import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot


# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.num_list = []
        self.num = ""
        self.action = ""
        self.GUI()
        self.darkMode = False


    # Buttons press actions
    def button_press(self):
        if self.action == "-":
            self.num_list.append(float(self.num) * -1)

        elif self.action == "+":
            self.num_list.append(float(self.num))
        
        elif self.action == "*":
            self.num = self.num_list[len(self.num_list) - 1] * float(self.num)
            self.num_list.remove(self.num_list[len(self.num_list) - 1])
            self.num_list.append(float(self.num))

        elif self.action == "/":
            self.num = self.num_list[len(self.num_list) - 1] / float(self.num)
            self.num_list.remove(self.num_list[len(self.num_list) - 1])
            self.num_list.append(float(self.num))

        elif self.action == "!":
            self.number = float(self.num)
            self.number2 = float(self.num)
            while self.number > 1:
                self.number -= 1
                self.number2 *= self.number
            
            self.num_list.remove(self.num_list[len(self.num_list) - 1])
            self.num_list.append(self.number2)
        
        else:
            self.num_list.append(float(self.num))


    # The GUI
    def GUI(self):
        # Styles of calculator
        self.light = """

        QMainWindow {
                background: #fff;
        }

        QLabel {
                background: #eee;
                color: #000;
                border: 0px;
                padding: 10px;
        }

        QPushButton {
                background: #eee;
                color: #000;
                border: 0px;
        }

        QPushButton:hover {
                background: #ddd;
        }

        QPushButton:pressed {
                background: #5599ff;
        }

        QMessageBox {
                background: #fff;
        }

        QMessageBox QPushButton {
                height: auto;
                width: auto;
        }

        QMessageBox QLabel {
                background: #fff;
                color: #000;
                border: 0px;
                padding: 10px;
        }
        """

        self.dark = """

            QMainWindow {
                    background: #000;
            }

            QLabel {
                    background: #111;
                    color: #fff;
                    border: 0px;
                    padding: 10px;
            }

            QPushButton {
                    background: #111;
                    color: #fff;
                    border: 0px;
            }

            QPushButton:hover {
                    background: #222;
            }

            QPushButton:pressed {
                    background: #5599ff;
            }

            QMessageBox {
                    background: #000;
            }

            QMessageBox QPushButton {
                    height: auto;
                    width: auto;
            }

            QMessageBox QLabel {
                    background: #000;
                    color: #fff;
                    border: 0px;
                    padding: 10px;
            }
            """


        self.setWindowTitle("Calculator")
        self.setFixedSize(420, 180)
        self.setStyleSheet(self.light)
        
        
        # Label
        self.label = QLabel("", self)
        self.label.move(10, 10)
        self.label.setFixedWidth(400)


        # Dark mode
        self.darkButton = QPushButton("🌑", self)
        self.darkButton.move(380, 10)
        self.darkButton.setFixedSize(30, 30)
        self.darkButton.setToolTip("Dark mode")
        self.darkButton.clicked.connect(self.dark_click)


        # Number buttons
        self.num1 = QPushButton("1", self)
        self.num1.move(10, 50)
        self.num1.clicked.connect(self.num1_click)

        self.num2 = QPushButton("2", self)
        self.num2.move(110, 50)
        self.num2.clicked.connect(self.num2_click)

        self.num3 = QPushButton("3", self)
        self.num3.move(210, 50)
        self.num3.clicked.connect(self.num3_click)

        self.num4 = QPushButton("4", self)
        self.num4.move(10, 80)
        self.num4.clicked.connect(self.num4_click)

        self.num5 = QPushButton("5", self)
        self.num5.move(110, 80)
        self.num5.clicked.connect(self.num5_click)

        self.num6 = QPushButton("6", self)
        self.num6.move(210, 80)
        self.num6.clicked.connect(self.num6_click)

        self.num7 = QPushButton("7", self)
        self.num7.move(10, 110)
        self.num7.clicked.connect(self.num7_click)

        self.num8 = QPushButton("8", self)
        self.num8.move(110, 110)
        self.num8.clicked.connect(self.num8_click)

        self.num9 = QPushButton("9", self)
        self.num9.move(210, 110)
        self.num9.clicked.connect(self.num9_click)

        self.num0 = QPushButton("0", self)
        self.num0.move(10, 140)
        self.num0.clicked.connect(self.num0_click)


        # Action buttons
        self.add = QPushButton("+", self)
        self.add.move(110, 140)
        self.add.clicked.connect(self.add_click)

        self.sub = QPushButton("-", self)
        self.sub.move(210, 140)
        self.sub.clicked.connect(self.sub_click)

        self.mul = QPushButton("x", self)
        self.mul.move(310, 50)
        self.mul.clicked.connect(self.mul_click)

        self.div = QPushButton("/", self)
        self.div.move(310, 80)
        self.div.clicked.connect(self.div_click)

        self.fac = QPushButton("!", self)
        self.fac.move(310, 110)
        self.fac.clicked.connect(self.fac_click)

        self.resault = QPushButton("=", self)
        self.resault.move(310, 140)
        self.resault.clicked.connect(self.resault_click)


    # When the buttons pressed
    @pyqtSlot()
    def num1_click(self):
        if self.action != "!":
            self.num += "1"
            self.label.setText(self.label.text() + "1")
        
        else:
            pass

    def num2_click(self):
        if self.action != "!":
            self.num += "2"
            self.label.setText(self.label.text() + "2")
        
        else:
            pass
    
    def num3_click(self):
        if self.action != "!":
            self.num += "3"
            self.label.setText(self.label.text() + "3")
        
        else:
            pass

    def num4_click(self):
        if self.action != "!":
            self.num += "4"
            self.label.setText(self.label.text() + "4")
        
        else:
            pass

    def num5_click(self):
        if self.action != "!":
            self.num += "5"
            self.label.setText(self.label.text() + "5")
        
        else:
            pass

    def num6_click(self):
        if self.action != "!":
            self.num += "6"
            self.label.setText(self.label.text() + "6")
        
        else:
            pass

    def num7_click(self):
        if self.action != "!":
            self.num += "7"
            self.label.setText(self.label.text() + "7")
        
        else:
            pass

    def num8_click(self):
        if self.action != "!":
            self.num += "8"
            self.label.setText(self.label.text() + "8")
        
        else:
            pass

    def num9_click(self):
        if self.action != "!":
            self.num += "9"
            self.label.setText(self.label.text() + "9")
        
        else:
            pass

    def num0_click(self):
        if self.action != "!":
            self.num += "0"
            self.label.setText(self.label.text() + "0")
        
        else:
            pass


    # If addition button pressed
    def add_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " + ")

            self.button_press()
                
            self.num = ""
            self.action = "+"
        
        else:
            pass


    # If subtraction button pressed
    def sub_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " - ")

            self.button_press()
                
            self.num = ""
            self.action = "-"
        
        else:
            pass


    # If multiplication button pressed
    def mul_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " x ")

            self.button_press()
                
            self.num = ""
            self.action = "*"
        
        else:
            pass


    # If division button pressed
    def div_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " / ")

            self.button_press()
                
            self.num = ""
            self.action = "/"
        
        else:
            pass


    # If factorial button pressed
    def fac_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + "!")

            self.button_press()
                
            self.action = "!"
 

    # If resault button pressed
    def resault_click(self):
        if self.num != "":
            self.button_press()

            self.num = str(sum(self.num_list))
            self.resault_msg = QMessageBox.question(self, "Resault", "The resault is: {}".format(self.num), QMessageBox.Ok, QMessageBox.Ok)
            self.action = ""
            self.num_list = []
            self.num = ""
            self.label.setText("")
        
        else:
            pass

    
    # If dark mode button pressed
    def dark_click(self):
        if self.darkMode == False:
            self.setStyleSheet(self.dark)
            self.darkMode = True
            self.darkButton.setText("🌕")
        
        else:
            self.setStyleSheet(self.light)
            self.darkButton.setText("🌑")
            self.darkMode = False


# appliaction
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()