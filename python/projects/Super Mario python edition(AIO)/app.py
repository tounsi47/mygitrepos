#This very big comment is redirecting to anyone who's reading it.
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
#This program is published by the OpenJasmine individual project
#Copyright OpenJasmine 2024
#This was a part of my expressions and feeling, now we are passing to the serious :)


#Importing required modules for the AIO game
from PyQt5.QtCore import Qt #The essential module to run a PyQT5 based app
from PyQt5.QtWidgets import *#To create widgets like windows , PushButton , labels....
from PyQt5.QtGui import * #configure the theme of the widgets
'''THe PyQt5 module will be used ONLY FOR THE MENU AND THE GAME SETTINGS'''




'''First part: creating the game menu and the game settings'''
'''Definition : When you will run the file, the firts window will apeear is the game menu,
this menu will ask you to do the following things:
-Quit : quit the programm
-Play : the menu will be closed and it will run the game
- Configure : will open the game settings to configure the game
-about : showing information  about the game (version, details ...) '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
core_app = QApplication([])
#defining functions that we'll use them for this python file
def connect_game():
    pass
def open_info():
    about.show()
    
def open_game_settings():
    pass
#The main PyQT5 compenment

#creating and configuring the window
window = QWidget()
window.resize(500 , 200)
#Adding layouts:
main_layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()## this 2 seconds layout will be added to the main one
#creating the label and the buttons :
label = QLabel('Welcome to the super mario game')#this widget will be added to layout 1
btn_exit = QPushButton('Exit')
btn_exit.clicked.connect(exit)# when the user will click to the (exit) button, the app will be closed
btn_play = QPushButton('PLay!!!')
btn_play.clicked.connect(connect_game)# when the user click to this button, the menu will be closed, then the game will be appeared
btn_about = QPushButton('About...')
btn_about.clicked.connect(open_info)#to show the information about the game
btn_settings = QPushButton('Settings')# the 4 last buttons will be added in layout 2
btn_settings.clicked.connect(open_game_settings)
#settings up the widgets to the layouts
layout1.addWidget(label, alignment=Qt.AlignCenter)
layout2.addWidget(btn_exit)
layout2.addWidget(btn_play)
layout2.addWidget(btn_settings)
layout2.addWidget(btn_about)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
#setting up the windows with the main layout
window.setLayout(main_layout)
#running the app and showing the window
window.show()

'''Part 2 creating the about window
THis window will show informations about the game'''
about = QWidget()
about.resize(1000 , 500)
#creating Widgets
label = QLabel('Super Mario python edition')
font = QFont('Arial', 36 , True)
label.setFont(font)

label2 = QLabel('This programm is made by the OpenJasmine individual project with the python and its modules(pygame, qt, time and random)')
layout = QVBoxLayout()
layout.addWidget(label, alignment = Qt.AlignCenter)
layout.addWidget(label2, alignment = Qt.AlignCenter)
about.setLayout(layout)


#This last line is to run the core app
core_app.exec_()





