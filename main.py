import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QCheckBox, QLabel
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Project Creator")
    project_name_value = None

    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    layout_1 = QHBoxLayout()
    layout_2 = QHBoxLayout()
    layout_3 = QHBoxLayout()
    layout_4 = QHBoxLayout()
    layout_5 = QHBoxLayout()
    layout_6 = QHBoxLayout()
    layout_7 = QHBoxLayout()
    layout_8 = QHBoxLayout()

    label = QLabel('Enter Project Name:')
    label_2 = QLabel('Services')
    label_2.setAlignment(Qt.AlignCenter)
    label_3 = QLabel('Folders')
    label_3.setAlignment(Qt.AlignCenter)
    project_name = QLineEdit()
    button_1 = QPushButton("Click Me!")
    button_2 = QPushButton("Click Me Too!")
    checkbox_1 = QCheckBox('Service 1')
    checkbox_2 = QCheckBox('Service 2')
    checkbox_3 = QCheckBox('Service 3')
    checkbox_4 = QCheckBox('Service 4')
    checkbox_5 = QCheckBox('Service 5')
    checkbox_6 = QCheckBox('Service 6')
    checkbox_7 = QCheckBox('Folder 1')
    checkbox_8 = QCheckBox('Folder 2')
    
    layout_1.addWidget(label)
    layout_1.addWidget(project_name)
    layout_2.addWidget(label_2)
    layout_3.addWidget(checkbox_1)
    layout_3.addWidget(checkbox_2)
    layout_4.addWidget(checkbox_3)
    layout_4.addWidget(checkbox_4)
    layout_5.addWidget(checkbox_5)
    layout_5.addWidget(checkbox_6)
    layout_6.addWidget(label_3)
    layout_7.addWidget(checkbox_7)
    layout_7.addWidget(checkbox_8)
    layout_8.addWidget(button_1)
    layout_8.addWidget(button_2)

    layout.addLayout(layout_1)
    layout.addLayout(layout_2)
    layout.addLayout(layout_3)
    layout.addLayout(layout_4)
    layout.addLayout(layout_5)
    layout.addLayout(layout_6)
    layout.addLayout(layout_7)
    layout.addLayout(layout_8)

    window.setCentralWidget(central_widget)
    window.show()

    def on_button_1_clicked():
        nonlocal project_name_value
        project_name_value = project_name.text()
    
    button_1.clicked.connect(on_button_1_clicked)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
