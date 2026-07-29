# Source Generated with Decompyle++
# File: task4.pyc (Python 3.9)

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from random import shuffle
true = [
    'анонИм',
    'асимметрИя',
    'бАнты',
    'балОванный',
    'балУясь',
    'блАговест',
    'вдовствО',
    'ветеринАрия',
    'включЁнный',
    'включИм',
    'вручИт',
    'гЕрбовый',
    'гастронОмия',
    'грошОвый',
    'дОверху',
    'давнИшний',
    'докраснА',
    'духовнИк',
    'еретИк',
    'жалюзИ',
    'зАгнутый',
    'завИдно',
    'закУпорить',
    'знАмение',
    'зубчАтый',
    'Иконопись',
    'Иксы',
    'издрЕвле',
    'исчЕрпать',
    'кАмбала',
    'кУхонный',
    'квартАл',
    'клАла',
    'мастерскИ',
    'мозаИчный',
    'нАискось',
    'обеспЕчение',
    'плЕсневеть',
    'свЁкла',
    'сверлИт',
    'сирОты',
    'слИвовый',
    'фетИш',
    'ходАтайство',
    'щавЕль',
    'щемИт']
false = [
    'анОним',
    'асиммЕтрия',
    'бантЫ',
    'бАлованный',
    'бАлуясь',
    'благовЕст',
    'вдОвство',
    'ветеренарИя',
    'вклЮченный',
    'вклЮчим',
    'врУчит',
    'гербОвый',
    'гастрономИя',
    'грОшовый',
    'довЕрху',
    'дАвнишний',
    'дОкрасна',
    'духОвник',
    'ерЕтик',
    'жАлюзи',
    'загнУтый',
    'зАвидно',
    'закупОрить',
    'знамЕние',
    'зУбчатый',
    'икОнопись',
    'иксЫ',
    'Издревле',
    'исчерпАть',
    'камбалА',
    'кухОнный',
    'квАртал',
    'клалА',
    'мАстерски',
    'мозАичный',
    'наИскось',
    'обеспечЕние',
    'плесневЕть',
    'свеклА',
    'свЕрлит',
    'сИроты',
    'сливОвый',
    'фЕтиш',
    'ходатАйство',
    'щАвель',
    'щЕмит']
k = 0
record = 0

class Ui_MainWindow(object):
    k = 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(793, 812)
        MainWindow.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.49505, y1:0.017, x2:0.5, y2:0.938, stop:0.0497512 rgba(249, 239, 216, 209), stop:1 rgba(255, 180, 213, 245));\n')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(24)
        self.centralwidget.setObjectName('centralwidget')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 651, 301))
        self.pushButton.setStyleSheet('background-color: rgb(254, 255, 233);')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 470, 651, 301))
        self.pushButton_2.setStyleSheet('background-color: rgb(254, 255, 233);')
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 300, 41))
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.label.setObjectName('label')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 40, 300, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.label_2.setObjectName('label')
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

    
    def retranslateUi(self, MainWindow):
        n = randint(0, len(true)) - 1
        variants = [
            true[n],
            false[n]]
        shuffle(variants)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'Задание 4. Ударения'))
        self.pushButton.setText(_translate('MainWindow', variants[0]))
        self.pushButton_2.setText(_translate('MainWindow', variants[1]))
        self.label.setText(_translate('MainWindow', 'Счёт: 0'))
        self.label_2.setText(_translate('MainWindow', 'Рекорд: 0'))

    
    def add_functions(self):
        self.pushButton.clicked.connect(self.change1)
        self.pushButton_2.clicked.connect(self.change2)

    
    def change1(self):
        global k, record, k
        _translate = QtCore.QCoreApplication.translate
        if self.pushButton.text() in true:
            k += 1
        elif k > record:
            record = k
            self.label_2.setText(_translate('MainWindow', str('Рекорд: ' + str(record))))
        k = 0
        self.label.setText(_translate('MainWindow', str('Счёт: ' + str(k))))
        n = randint(0, len(true)) - 1
        variants = [
            true[n],
            false[n]]
        shuffle(variants)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate('MainWindow', variants[0]))
        self.pushButton_2.setText(_translate('MainWindow', variants[1]))

    
    def change2(self):
        global k, record, k
        _translate = QtCore.QCoreApplication.translate
        if self.pushButton_2.text() in true:
            k += 1
        elif k > record:
            record = k
            self.label_2.setText(_translate('MainWindow', str('Рекорд: ' + str(record))))
        k = 0
        self.label.setText(_translate('MainWindow', str('Счёт: ' + str(k))))
        n = randint(0, len(true)) - 1
        variants = [
            true[n],
            false[n]]
        shuffle(variants)
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate('MainWindow', variants[0]))
        self.pushButton_2.setText(_translate('MainWindow', variants[1]))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
