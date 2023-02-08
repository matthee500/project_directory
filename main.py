import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QCheckBox

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PySide6 GUI Example")

central_widget = QWidget()
layout = QVBoxLayout(central_widget)
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()
layout_4 = QHBoxLayout()
layout_5 = QHBoxLayout()

button_1 = QPushButton("Click Me!")
button_2 = QPushButton("Click Me Too!")
checkbox_1 = QCheckBox('Option 1')
checkbox_2 = QCheckBox('Option 2')
checkbox_3 = QCheckBox('Option 3')
checkbox_4 = QCheckBox('Option 4')
checkbox_5 = QCheckBox('Option 5')
checkbox_6 = QCheckBox('Option 6')
combo = QComboBox()

combo.addItem('Item_1')
combo.addItem('Item_2')
combo.addItem('Item_3')

layout_2.addWidget(checkbox_1)
layout_2.addWidget(checkbox_2)
layout_3.addWidget(checkbox_3)
layout_3.addWidget(checkbox_4)
layout_4.addWidget(checkbox_5)
layout_4.addWidget(checkbox_6)
layout_5.addWidget(button_1)
layout_5.addWidget(button_2)

layout.addWidget(combo)
layout.addLayout(layout_2)
layout.addLayout(layout_3)
layout.addLayout(layout_4)
layout.addLayout(layout_5)

window.setCentralWidget(central_widget)
window.show()
sys.exit(app.exec())
