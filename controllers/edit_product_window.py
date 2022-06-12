from PySide2.QtWidgets import QtWidgets
from views.edit_product import Editar_producto

class Editar_producto_window(QtWidgets, Editar_producto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def populate_input(self):
        pass
    def select_file(self):
        pass
    def check_input(self):
        pass
    def edit_producto(self):
        pass
