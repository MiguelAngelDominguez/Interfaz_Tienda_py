from PySide2.QtWidgets import QtWidgets
from views.new_product import Nuevo_producto

class Nuevo_producto_Window(QtWidgets, Nuevo_producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def check_input(self):
        pass
    def add_producto(self):
        pass
    def clean_input(self):
        pass
    def select_file(self):
        pass
    def undo(self):
        pass