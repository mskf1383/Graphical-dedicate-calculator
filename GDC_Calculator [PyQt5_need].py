"""by MSKF"""


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot
from math import sqrt


# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.num_list = []
        self.num = ""
        self.action = ""
        self.darkMode = False
        self.sqrt = False
        self.sign = "+"
        self.signuse = False
        self.GUI()
        

    # Buttons press actions
    def button_press(self):
        try:
            # Sqrt
            if self.sqrt == True:
                self.num = str(sqrt(float(self.num)))
                self.sqrt = False
            
            # Sign
            if self.sign == "-":
                self.num = str(float(self.num) * -1)
                self.label1.setText(self.label1.text() + ")")
                self.sign = "+"
                self.signuse = False

            # If action is subtraction
            if self.action == "-":
                self.num_list.append(float(self.num) * -1)

            # If action is addition
            elif self.action == "+":
                self.num_list.append(float(self.num))
            
            # If action is multiplication
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * float(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(float(self.num))

            # If action is division
            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / float(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(float(self.num))

            # If action is factorial
            elif self.action == "!":
                self.number = float(self.num)
                self.number2 = float(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                    
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)

            # If none of them
            else:
                self.num_list.append(float(self.num))
        
        except:
            pass

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
                font-size: 16px;
        }

        self.label1{
            background: #000;
        }

        QPushButton {
                background: #eee;
                color: #000;
                border: 0px;
                padding: 10px;
                font-size: 16px;
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
                    font-size: 16px;
            }

            QPushButton {
                    background: #111;
                    color: #fff;
                    border: 0px;
                    padding: 10px;
                    font-size: 16px;
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
        self.setFixedSize(330, 320)
        self.setStyleSheet(self.light)
        
        
        # Labels
        self.label1 = QLabel("", self)
        self.label1.move(10, 10)
        self.label1.setFixedSize(310, 40)
        self.label1.setStyleSheet("font-size: 16px;")

        self.label2 = QLabel("", self)
        self.label2.move(10, 50)
        self.label2.setFixedSize(310, 50)
        self.label2.setStyleSheet("font-size: 20px;")


        # Dark mode
        self.darkButton = QPushButton("🌑", self)
        self.darkButton.move(270, 50)
        self.darkButton.setFixedSize(50, 50)
        self.darkButton.setToolTip("Dark mode: {}".format("off" if self.darkMode == False else "on"))
        self.darkButton.clicked.connect(self.dark_click)


        # Number buttons
        self.num1 = QPushButton("1", self)
        self.num1.move(10, 110)
        self.num1.setFixedSize(50, 50)
        self.num1.clicked.connect(self.num1_click)

        self.num2 = QPushButton("2", self)
        self.num2.move(60, 110)
        self.num2.setFixedSize(50, 50)
        self.num2.clicked.connect(self.num2_click)

        self.num3 = QPushButton("3", self)
        self.num3.move(110, 110)
        self.num3.setFixedSize(50, 50)
        self.num3.clicked.connect(self.num3_click)

        self.num4 = QPushButton("4", self)
        self.num4.move(10, 160)
        self.num4.setFixedSize(50, 50)
        self.num4.clicked.connect(self.num4_click)

        self.num5 = QPushButton("5", self)
        self.num5.move(60, 160)
        self.num5.setFixedSize(50, 50)
        self.num5.clicked.connect(self.num5_click)

        self.num6 = QPushButton("6", self)
        self.num6.move(110, 160)
        self.num6.setFixedSize(50, 50)
        self.num6.clicked.connect(self.num6_click)

        self.num7 = QPushButton("7", self)
        self.num7.move(10, 210)
        self.num7.setFixedSize(50, 50)
        self.num7.clicked.connect(self.num7_click)

        self.num8 = QPushButton("8", self)
        self.num8.move(60, 210)
        self.num8.setFixedSize(50, 50)
        self.num8.clicked.connect(self.num8_click)

        self.num9 = QPushButton("9", self)
        self.num9.move(110, 210)
        self.num9.setFixedSize(50, 50)
        self.num9.clicked.connect(self.num9_click)

        self.num0 = QPushButton("0", self)
        self.num0.move(60, 260)
        self.num0.setFixedSize(50, 50)
        self.num0.clicked.connect(self.num0_click)

        self.dot = QPushButton("·", self)
        self.dot.move(110, 260)
        self.dot.setFixedSize(50, 50)
        self.dot.clicked.connect(self.dot_click)

        self.sig = QPushButton("+/-", self)
        self.sig.move(10, 260)
        self.sig.setFixedSize(50, 50)
        self.sig.clicked.connect(self.sign_click)


        # Action buttons
        self.clean = QPushButton("Clean", self)
        self.clean.move(170, 110)
        self.clean.setFixedSize(100, 50)
        self.clean.clicked.connect(self.clean_click)

        self.add = QPushButton("+", self)
        self.add.move(170, 160)
        self.add.setFixedSize(50, 50)
        self.add.clicked.connect(self.add_click)

        self.sub = QPushButton("-", self)
        self.sub.move(220, 160)
        self.sub.setFixedSize(50, 50)
        self.sub.clicked.connect(self.sub_click)

        self.mul = QPushButton("×", self)
        self.mul.move(170, 210)
        self.mul.setFixedSize(50, 50)
        self.mul.clicked.connect(self.mul_click)

        self.div = QPushButton("÷", self)
        self.div.move(220, 210)
        self.div.setFixedSize(50, 50)
        self.div.clicked.connect(self.div_click)

        self.fac = QPushButton("!", self)
        self.fac.move(270, 110)
        self.fac.setFixedSize(50, 50)
        self.fac.clicked.connect(self.fac_click)

        self.rad = QPushButton("√", self)
        self.rad.move(270, 160)
        self.rad.setFixedSize(50, 50)
        self.rad.clicked.connect(self.rad_click)

        self.resault = QPushButton("=", self)
        self.resault.move(170, 260)
        self.resault.setFixedSize(100, 50)
        self.resault.clicked.connect(self.resault_click)


    # When the buttons pressed
    @pyqtSlot()
    def num1_click(self):
        if self.action != "!":
            self.num += "1"
            self.label2.setText(self.label2.text() + "1")
        
        else:
            pass

    def num2_click(self):
        if self.action != "!":
            self.num += "2"
            self.label2.setText(self.label2.text() + "2")
        
        else:
            pass
    
    def num3_click(self):
        if self.action != "!":
            self.num += "3"
            self.label2.setText(self.label2.text() + "3")
        
        else:
            pass

    def num4_click(self):
        if self.action != "!":
            self.num += "4"
            self.label2.setText(self.label2.text() + "4")
        
        else:
            pass

    def num5_click(self):
        if self.action != "!":
            self.num += "5"
            self.label2.setText(self.label2.text() + "5")
        
        else:
            pass

    def num6_click(self):
        if self.action != "!":
            self.num += "6"
            self.label2.setText(self.label2.text() + "6")
        
        else:
            pass

    def num7_click(self):
        if self.action != "!":
            self.num += "7"
            self.label2.setText(self.label2.text() + "7")
        
        else:
            pass

    def num8_click(self):
        if self.action != "!":
            self.num += "8"
            self.label2.setText(self.label2.text() + "8")
        
        else:
            pass

    def num9_click(self):
        if self.action != "!":
            self.num += "9"
            self.label2.setText(self.label2.text() + "9")
        
        else:
            pass

    def num0_click(self):
        if self.action != "!":
            self.num += "0"
            self.label2.setText(self.label2.text() + "0")
        
        else:
            pass

    def dot_click(self):
        if self.action != "!":
            self.num += "."
            self.label2.setText(self.label2.text() + ".")
        
        else:
            pass

    def sign_click(self):
        if self.num == "":
            if self.signuse == False:
                if self.sign == "+":
                    self.sign = "-"
                    self.label2.setText(self.label2.text() + "-(")
                    self.signuse = True

                else:
                    self.sign = "+"
                    self.label2.setText(self.label2.text() + "+(")
                    self.signuse = True
            
            else:
                if self.sign == "+":
                    self.sign = "-"
                    x = self.label2.text()
                    x = self.label2.text()[:len(x) - 2]
                    self.label2.setText(x + "-(")
                    self.signuse = True

                else:
                    self.sign = "+"
                    x = self.label2.text()
                    x = self.label2.text()[:len(x) - 2]
                    self.label2.setText(x + "+(")
                    self.signuse = True


    # If addition button pressed
    def add_click(self):
        if "=" in self.label1.text():
            self.action = ""
            self.num_list = []
            self.label1.setText("")
            self.sign = "+"
            self.signuse = False
            self.sqrt = False

            self.label1.setText(self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " + ")
            self.label2.setText("")

            self.num = ""
            self.action = "+"

        elif self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " + ")
            self.label2.setText("")
                
            self.num = ""
            self.action = "+"
        
        else:
            pass


    # If subtraction button pressed
    def sub_click(self):
        if "=" in self.label1.text():
            self.action = ""
            self.num_list = []
            self.label1.setText("")
            self.sign = "+"
            self.signuse = False
            self.sqrt = False

            self.label1.setText(self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " - ")
            self.label2.setText("")

            self.num = ""
            self.action = "-"

        elif self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " - ")
            self.label2.setText("")
                
            self.num = ""
            self.action = "-"
        
        else:
            pass


    # If multiplication button pressed
    def mul_click(self):
        if "=" in self.label1.text():
            self.action = ""
            self.num_list = []
            self.label1.setText("")
            self.sign = "+"
            self.signuse = False
            self.sqrt = False

            self.label1.setText(self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " × ")
            self.label2.setText("")

            self.num = ""
            self.action = "*"

        elif self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " × ")
            self.label2.setText("")
                
            self.num = ""
            self.action = "*"
        
        else:
            pass


    # If division button pressed
    def div_click(self):
        if "=" in self.label1.text():
            self.action = ""
            self.num_list = []
            self.label1.setText("")
            self.sign = "+"
            self.signuse = False
            self.sqrt = False

            self.label1.setText(self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " ÷ ")
            self.label2.setText("")

            self.num = ""
            self.action = "/"

        elif self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " ÷ ")
            self.label2.setText("")
                
            self.num = ""
            self.action = "/"
        
        else:
            pass


    # If factorial button pressed
    def fac_click(self):
        if "=" in self.label1.text():
            self.action = ""
            self.num_list = []
            self.label1.setText("")
            self.sign = "+"
            self.signuse = False
            self.sqrt = False

            self.label1.setText(self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + "!")
            self.label2.setText("")

            self.action = "!"

        elif self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + "!")
            self.label2.setText("")

            self.action = "!"

    
    def rad_click(self):
        if self.label2.text() == "":
            self.label2.setText(self.label2.text() + "√")

        if self.label2.text()[len(self.label2.text()) - 1] != "√":
            self.label2.setText(self.label2.text() + "√")

        self.sqrt = True
 

    # If resault button pressed
    def resault_click(self):
        if self.num != "":
            self.label1.setText(self.label1.text() + self.label2.text())
            self.button_press()
            self.label1.setText(self.label1.text() + " = ")
            self.num = str(sum(self.num_list))
            self.label2.setText(self.num)
            self.action = ""
            self.num_list = []
            self.sign = "+"
            self.signuse = False
            self.sqrt = False
        
        else:
            pass


    # If clean button pressed
    def clean_click(self):
        self.action = ""
        self.num_list = []
        self.label1.setText("")
        self.label2.setText("")
        self.num = ""
        self.sign = "+"
        self.signuse = False
        self.sqrt = False

    
    # If dark mode button pressed
    def dark_click(self):
        if self.darkMode == False:
            self.darkMode = True
        
        else:
            self.darkMode = False
        
        self.setStyleSheet(self.light if self.darkMode == False else self.dark)
        self.darkButton.setText("🌑" if self.darkMode == False else "🌕")
        self.darkButton.setToolTip("Dark mode: {}".format("off" if self.darkMode == False else "on"))


# appliaction
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
