import sys
import random
from PySide2.QtWidgets import (QApplication, QWidget, QHBoxLayout, QPushButton,
                               QLabel)


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.button = QPushButton("Random")
        self.label = QLabel("0")

        self.button.clicked.connect(self.randomize)

        layout = QHBoxLayout()
        layout.addWidget(self.label, 1)
        layout.addWidget(self.button, 1)

        self.setLayout(layout)

    def randomize(self):
        self.label.setText(f"{random.randint(0,100)}")

if __name__ == "__main__":
    app = QApplication()
    widget = Widget()
    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec_())
