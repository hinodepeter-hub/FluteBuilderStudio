from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from . import __version__


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Flute Builder Studio {__version__}")
        self.resize(1200, 800)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
