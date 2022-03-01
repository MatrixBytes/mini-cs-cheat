from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from threading import Thread
from pynput.keyboard import Controller as keyboard_controller
from pynput.mouse import Controller as mouse_controller
from pynput.mouse import Listener, Button
from time import sleep

def ez():
    keyboard = keyboard_controller()
    mouse = mouse_controller()

    def peekshot_right():
        keyboard.press('d')
        sleep(0.2)
        keyboard.release('d')
        sleep(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)

    def peekshot_left():
        keyboard.press('a')
        sleep(0.2)
        keyboard.release('a')
        sleep(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)

    def click(x, y, button, pressed):
        if not pressed:
            button = str(button)
            if button == 'Button.button9':
                peekshot_right()
            if button == 'Button.button8':
                peekshot_left()

    with Listener(on_click = click) as listener:
        listener.join()

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent = None, windowSize = 0, penWidth = 0):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor(255,255,255,255))          
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))

    def paintEvent(self, event):
        ws = self.ws
        d = 6
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(ws/2, 0, ws/2, ws/2 - ws/d)
        painter.drawLine(ws/2, ws/2 + ws/d, ws/2, ws)
        painter.drawLine(0, ws/2, ws/2 - ws/d, ws/2)
        painter.drawLine(ws/2 + ws/d, ws/2, ws, ws/2)

app = QtWidgets.QApplication(sys.argv) 

widget = Crosshair(windowSize = 24, penWidth = 2)
widget.show()

Thread(target = ez).start()

sys.exit(app.exec_())
