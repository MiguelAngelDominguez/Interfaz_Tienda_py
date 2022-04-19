from Pyside2.QtWidgets import QWidget
from views.main_window import Tienda_Main

class ListProductWindow(QWidget,Tienda_main):
    def __init__(self):
        super().__init__()