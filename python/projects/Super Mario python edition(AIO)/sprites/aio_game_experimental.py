'''Dear programmer ... Do you know how high level programming is to hard?
I'm not talking about easy thing, like building a simple python calculator in a console...
I'm talking about a professionnal thing, like this : build a python game and a modulable and customizable one,
 and do not think that I'm genius to do this thing
I just want to improve my python skills, that all, and I'm sure that in a certain error when running the file,
I will use the Net or even ChatGPT
I'm sure that at any moment I will meet a problem in the programm's syntax, or meet a python problem in my computer,
 espacially because I run linux ...
And by the way, I also think about building an LFS system, or even a system with my own kernel, 
everyone who will try that will say (This is the hell.... Im' retiring!!)
-How could Bill Gates and Paul Allen, the PDGs of Microsoft, make their own operating system starting from Windows 1.0 (1985) to
 the actual one (Windows 11, 2024), with its great and evolved appearance and its great performance for new laptops and computers?
-How Steve Jobs could make his enterprise Apple and make the most elegant OS for MacBooks and iMacs and such more...
-How AliBaba could make his big enterprise for world exchange (AliExpress) after a lot of pain and losses
-How can I create my own Linux operating system, with its own package manager,
 with something that lets it run Windows apps correctly, with an adapted interface for all kinds of computers????? And now I'm just
building a simple 2D game??!
The answer : Because they never retire, instead of panic, they search about the problem and learn from it,
 if they buid something very big so that never means that
they are better than us, no one is perfetc...
They are hust like us,  they already do errors, but instead of retiring, they do their best to correct the error and learn from it,
this is the real programmer!
And this is the source of experiences in technology ...
Not just in python, but in anythings, even out of informatic !
However, just take this advice , and good luck !! 8)'''
#Importing all required modules
#Modules used to program the graphical interface of the app
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#Modules used to program the main game
from pygame import *
from random import *
from time import time as timer
#defining functions inside the AIO source file
 

def about():
    winabout = QMessageBox()
    winabout.setWindowTitle('About SMBPE')
    btn_close = QPushButton('Close')
    btn_close.clicked.connect(close)
    label = QLabel('Super mario bros Python Edition')
    label2 = QLabel('@The OpenJasmine individual project 2024')
    layou1 = QHBoxLayout()
    layou1.addWidget(btn_close)
    layou1.addWidget(label)
    layou1.addWidget(label2)
    winabout.setLayout(layou1)
    winabout.show()
    def close():
        global winabout
        winabout.quit()
#Phase 1 : creating the graphic Qt interface
app = QApplication([])
#a - creating the menu
menu = QWidget()
menu.resize(700, 500)
menu.setWindowTitle('Super Mario BROS Python edition')
btn_exit = QPushButton('Exit')
btn_play = QPushButton('Play')
btn_about = QPushButton('About')
btn_setting = QPushButton('Settings')
btn_exit.clicked.connect(exit)
btn_about.clicked.connect(about)
btn_play.clicked.connect()
btn_setting.clicked.connect()