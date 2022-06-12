from PySide2.QtWidgets import QWidget
from views.main_window import Tienda_Main

class Main_Window(QWidget,Tienda_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)    

    # Abrir Interfaz
    def open_ver_producto(self):
        pass
    def open_edit_producto(self):
        pass
    def open_new_producto(self):
        pass
    def open_config_producto(self):
        pass
    def open_ver_recibos(self):
        pass
    def open_edit_recibos(self):
        pass
    def open_new_recibos(self):
        pass
    def open_config_recibos(self):
        pass
    # Operaciones de Interfaz
    def new_producto(self):
        pass
    def edit_producto(self):
        pass
    def delete_producto(self):
        pass
    def buscar_producto(self):
        pass
    def actulizar_tabla_productos(self):
        pass
    def cancelar_operacion(self):
        pass
    #Funciones de Completado
    def populate_table(self):
        pass
    def populate_combobox(self):
        pass

    def search_product_by_name(self):
        pass
    def search_product_by_ID(self):
        pass
    def search_product_by_categoria(self):
        pass
    def search(self):
        pass

    def record_qt(self):
        pass
    