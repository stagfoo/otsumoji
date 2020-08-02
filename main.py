import sys
from PySide2 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("emoji/normal.png"))

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
# window.setWindowFlags(flags)

pixmap = QtGui.QPixmap('emoji/angry.png')
small = pixmap.scaled(240, 240, QtCore.Qt.KeepAspectRatio)
label = QtWidgets.QLabel()
label.setPixmap(small)
label.setWindowFlags(flags)
label.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
label.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
label.setFixedSize(240, 240)
label.move(1150, 680)

label.show()
app.exec_()
