import sys
from PySide2.QtCore import QStandardPaths, Qt
from PySide2.QtGui import QIcon, QKeySequence, QPixmap
from PySide2.QtWidgets import (QAction, QApplication, QDialog, QFileDialog,
    QMainWindow, QSlider, QStyle, QToolBar)
from PySide2.QtMultimediaWidgets import QVideoWidget

import rc_icons

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # ToolBar
        toolBar = QToolBar()

        playIcon = QIcon(QPixmap(":/icons/play.png"))
        previousIcon = QIcon(QPixmap(":/icons/previous.png"))
        pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
        nextIcon = QIcon(QPixmap(":/icons/forward.png"))
        stopIcon = QIcon(QPixmap(":/icons/stop.png"))

        self.playAction = toolBar.addAction(playIcon, "Play")
        self.previousAction = toolBar.addAction(previousIcon, "Previous")
        self.pauseAction = toolBar.addAction(pauseIcon, "Pause")
        self.nextAction = toolBar.addAction(nextIcon, "Next")
        self.stopAction = toolBar.addAction(stopIcon, "Stop")

        # Menu
        playMenu = self.menuBar().addMenu("&Play")
        playMenu.addAction(self.playAction)
        playMenu.addAction(self.previousAction)
        playMenu.addAction(self.pauseAction)
        playMenu.addAction(self.nextAction)
        playMenu.addAction(self.stopAction)

        self.addToolBar(toolBar)
        self.videoWidget = QVideoWidget()
        self.setCentralWidget(self.videoWidget)

        # Signals and Slots
        self.playAction.triggered.connect(self.play)

    def play(self):
        print("play")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.resize(800, 400)
    mainWin.show()
    sys.exit(app.exec_())
