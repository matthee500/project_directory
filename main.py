import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PySide6 GUI Example")

central_widget = QWidget()
layout = QVBoxLayout(central_widget)
button = QPushButton("Click Me!")
combo = QComboBox()

combo.addItem('Item_1')
combo.addItem('Item_2')
combo.addItem('Item_3')

layout.addWidget(combo)
layout.addWidget(button)

window.setCentralWidget(central_widget)
window.show()
sys.exit(app.exec())
