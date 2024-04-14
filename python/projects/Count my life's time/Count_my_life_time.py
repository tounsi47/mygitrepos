def second():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_second = entered_age * 31536000
    result = QMessageBox(win)
    result.setText(f'Your age in second is approximately:{age_in_second} seconds')
    result.show()
def minutes():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_minutes = entered_age * 525600
    result = QMessageBox(win)
    result.setText(f'Your age in minute is approximately:{age_in_minutes} minutes')
    result.show()
       

def hours():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_hours = entered_age * 8760
    result = QMessageBox(win)
    result.setText(f'Your age in hour is approximately:{age_in_hours} hours')
    result.show()
def weeks():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_weeks = entered_age * 52
    result = QMessageBox(win)
    result.setText(f'Your age in week is approximately:{age_in_weeks} weeks')
    result.show()
def days():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_days = entered_age * 365
    result = QMessageBox(win)
    result.setText(f'Your age in day is approximately:{age_in_days} days')
    result.show()
def months():
    while True:
        age, ok = QInputDialog.getText(win ,'Age input', 'Please enter your age')
        try :
            entered_age = int(age)
            break
        except :
            print('Error, you may type a integer.')
    print(entered_age)
    age_in_months = entered_age * 12
    result = QMessageBox(win)
    result.setText(f'Your age in month is approximately:{age_in_months} months')
    result.show()
       
    

def quit():
    win.hide()
    app.quit()
def about():
    font = QFont("Arial", 30, QFont.Bold)

    def close():
        info_win.hide()
    info_win = QWidget()
    info_win.setWindowTitle('About Cmlt')
    info_win.resize(1000 , 500)
    label  = QLabel("Count my life's time 1.0")
    label.setFont(font)
    label2 = QLabel("Based on python and designed with the Qt graphic librairie")
    label3 = QLabel('By Fury project 2024')
    ok = QPushButton('ok')
    layou = QVBoxLayout()
    layou.addWidget(label, alignment=Qt.AlignCenter)
    layou.addWidget(label2, alignment=Qt.AlignCenter)
    layou.addWidget(label3, alignment=Qt.AlignCenter)
    layou.addWidget(ok)
    info_win.setLayout(layou)
    info_win.show()
    ok.clicked.connect(close)
try :    
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont
    
    app = QApplication([])
    win = QWidget()
    win.setWindowTitle('Cmlt (Qt edition)')
    win.resize(1000, 500)
    quit_btn = QPushButton('quit')
    quit_btn.clicked.connect(quit)
    about_btn = QPushButton('about CMLT')
    about_btn.clicked.connect(about)
    label = QLabel('Select the conversion mode :')
    font = QFont("Arial", 12, QFont.Bold)
    label.setFont(font)

    sec_btn = QPushButton('Seconds')
    sec_btn.clicked.connect(second)
    min_btn = QPushButton('minutes')
    min_btn.clicked.connect(minutes)
    hrs_btn = QPushButton('hours')
    hrs_btn.clicked.connect(hours)
    dys_btn = QPushButton('days')
    dys_btn.clicked.connect(days)
    wks_btn = QPushButton('weeks')
    wks_btn.clicked.connect(weeks)
    mth_btn = QPushButton('months')
    mth_btn.clicked.connect(months)
    layou = QVBoxLayout()
    sub_layou0 = QHBoxLayout()
    sub_layou0.addWidget(quit_btn)
    sub_layou0.addWidget(about_btn)
    sub_layou1 = QHBoxLayout()
    sub_layou1.addWidget(label, alignment=Qt.AlignCenter)
    sub_layou2 = QHBoxLayout()
    sub_layou2.addWidget(sec_btn)
    sub_layou2.addWidget(min_btn)
    sub_layou2.addWidget(hrs_btn)
    sub_layou3 = QHBoxLayout()
    sub_layou3.addWidget(dys_btn)
    sub_layou3.addWidget(wks_btn)
    sub_layou3.addWidget(mth_btn)
    layou.addLayout(sub_layou0)
    layou.addLayout(sub_layou1)
    layou.addLayout(sub_layou2)
    layou.addLayout(sub_layou3)
    win.setLayout(layou)
    win.show()
    app.exec_()
except :
    print("Oops, a fatal error was happened since running the program")
    print('We suggest you some methods to fix this problem:')
    print('- if you are in windows , you should install the pyqt5 librairie , by typing (pip install PyQt5) in the command prompt or powershell')
    print("- if you are on macOS, it's recommended to use the homebrew and type (brew install pyqt5)" )
    print("- if you are in linux, if you work in console mode, you should work in a DE (such as Gnome, Plasma or other ..),  if you are in a console linux OS (such as free BSD or ubuntu server...), you can install a desktop environnement (Plasma is recommended as is based on Qt) ")
    print('However, you can use the programm without the GUI, would you want ? (y/n)')
    without_gui = input('>>')
    without_gui.lower()
    if without_gui == 'n'  :
        print('exiting ...')
    elif without_gui == 'y' :
        import non_gui_mode