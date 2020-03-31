"""by MSKF"""


import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.num_list = []
        self.num = ""
        self.action = ""
        self.GUI()

    def GUI(self):
        self.setWindowTitle("Calculator")
        self.resize(420, 180)

        self.label = QLabel("", self)
        self.label.move(20, 10)
        

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


    @pyqtSlot()
    def num1_click(self):
        self.num += "1"
        self.label.setText(self.label.text() + "1")

    def num2_click(self):
        self.num += "2"
        self.label.setText(self.label.text() + "2")
    
    def num3_click(self):
        self.num += "3"
        self.label.setText(self.label.text() + "3")

    def num4_click(self):
        self.num += "4"
        self.label.setText(self.label.text() + "4")

    def num5_click(self):
        self.num += "5"
        self.label.setText(self.label.text() + "5")

    def num6_click(self):
        self.num += "6"
        self.label.setText(self.label.text() + "6")

    def num7_click(self):
        self.num += "7"
        self.label.setText(self.label.text() + "7")

    def num8_click(self):
        self.num += "8"
        self.label.setText(self.label.text() + "8")

    def num9_click(self):
        self.num += "9"
        self.label.setText(self.label.text() + "9")

    def num0_click(self):
        self.num += "0"
        self.label.setText(self.label.text() + "0")

    def add_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " + ")

            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)
            
            else:
                self.num_list.append(int(self.num))
                
            self.num = ""
            self.action = "+"
        
        else:
            pass


    def sub_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " - ")

            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))
            
            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)

            else:
                self.num_list.append(int(self.num))
                
            self.num = ""
            self.action = "-"
        
        else:
            pass


    def mul_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " x ")

            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))
            
            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)
            
            else:
                self.num_list.append(int(self.num))
                
            self.num = ""
            self.action = "*"
        
        else:
            pass


    def div_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + " / ")

            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)
            
            else:
                self.num_list.append(int(self.num))
                
            self.num = ""
            self.action = "/"
        
        else:
            pass


    def fac_click(self):
        if self.num != "":
            self.label.setText(self.label.text() + "! ")

            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)
            
            else:
                self.num_list.append(int(self.num))
                
            self.action = "!"
 

    def resault_click(self):
        if self.num != "":
            if self.action == "-":
                self.num_list.append(int(self.num) * -1)

            elif self.action == "+":
                self.num_list.append(int(self.num))
            
            elif self.action == "*":
                self.num = self.num_list[len(self.num_list) - 1] * int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))

            elif self.action == "/":
                self.num = self.num_list[len(self.num_list) - 1] / int(self.num)
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(int(self.num))
            
            elif self.action == "!":
                self.number = int(self.num)
                self.number2 = int(self.num)
                while self.number > 1:
                    self.number -= 1
                    self.number2 *= self.number
                
                self.num_list.remove(self.num_list[len(self.num_list) - 1])
                self.num_list.append(self.number2)
            
            else:
                self.num_list.append(int(self.num))

            self.num = str(sum(self.num_list))
            self.resault_msg = QMessageBox.question(self, "Resault", "The resault is: {}".format(self.num), QMessageBox.Ok, QMessageBox.Ok)
            self.action = ""
            self.num_list = []
            self.num = ""
            self.label.setText("")
        
        else:
            pass



    
'''
    # Get the first number
    while True:
        num_list = []

        try:
            number = float(input("Enter a number: "))
            num_list.append(number)
            dialog = str(number)
            
            break
        
        # If the input undefind
        except ValueError:
            print("** Enter a number **")
            continue

    
    # Get the action
    while True:
        action = input("Enter the action (Press 'Enter' to finish): ")
        actions_list = ["+", "-", "*", "/", "!"]


        # Check the action
        if action.upper() == "":
            input("Resault: {}".format(sum(num_list)))
            
            app()

        elif action in actions_list:
            dialog = dialog + " " + action
            
            pass

        else:
            input("** Your action isn't avalable **")
            
            continue


        # Get the second number
        while True:
            if action != "!":
                try:
                    number = float(input("Enter a number: "))
                    dialog = dialog + " " + str(number)
                    
                    break
            
                # If the input undefind
                except ValueError:
                    input("** Enter a number **")
                    
                    continue
            
            else:
                break

        # Do the action
        if action == "+":
            num_list.append(number)

        elif action == "-":
            num_list.append(-number)

        elif action == "*":
            number *= num_list[len(num_list) - 1]
            num_list.remove(num_list[len(num_list) - 1])
            num_list.append(number)

        elif action == "/":
            if num_list[len(num_list) - 1] % number != 0.0:
                q = input("Do you like to round it? [yes/no] ")

                if q.lower() == "yes":
                    number = num_list[len(num_list) - 1] / number
                    num_list.remove(num_list[len(num_list) - 1])
                    number = flout(round(number))
                    num_list.append(number)

                else:
                    number = num_list[len(num_list) - 1] / number
                    num_list.remove(num_list[len(num_list) - 1])
                    num_list.append(number)

            else:
                number = num_list[len(num_list) - 1] / number
                num_list.remove(num_list[len(num_list) - 1])
                num_list.append(number)
            
        elif action == "!":
            num = number
            while num > 1:
                num -= 1
                number *= num
            
            num_list.remove(num_list[len(num_list) - 1])
            num_list.append(number)

'''


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()