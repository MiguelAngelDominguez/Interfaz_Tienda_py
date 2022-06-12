from PySide2.QtWidgets import QApplication
from controllers.main_window import Main_Window

if __name__ == '__main__':
    app = QApplication()
    window = Main_Window()
    window.show()
    app.exec_() 