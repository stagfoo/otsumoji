import sys
from PySide2 import QtCore, QtGui, QtWidgets
from inputs import devices, get_mouse, get_gamepad

def gamepadEvents():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.code, event.state)
            mainUI.show()
            mainUI.move(event.state, 680)
            mainWidget.exec_()


# Make the Window
mainWidget = QtWidgets.QApplication(sys.argv)
# Set the Window
mainWidget.setWindowIcon(QtGui.QIcon("emoji/normal.png"))

# Get Emoji and scale the emoji
emoji = QtGui.QPixmap('emoji/angry.png')
smallEmoji = emoji.scaled(240, 240, QtCore.Qt.KeepAspectRatio)

# Setup main UI
mainUI = QtWidgets.QLabel()
mainUI.setPixmap(smallEmoji)

# Make the window borderless
mainUI.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
mainUI.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
mainUI.setWindowFlags(flags)

# Size and Position of the window
mainUI.setFixedSize(240, 240)

gamepadEvents()
