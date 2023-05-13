print('Hello the world!')
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QtWidget, QPushButton, QLable, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_win = QtWidget()
main_win.setWindowTitle('')
main_win.move(900, 70)
main_win.resize(400, 200)



main_win.show()
app.exec_()
