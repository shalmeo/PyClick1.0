from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QKeyEvent

from app.controllers.main import Controller
from app.model.main import Model
from app.views.main_ui import Ui_MainWindow


class View(QMainWindow):
    def __init__(self, model: Model, controller: Controller) -> None:
        super().__init__()
        
        self._model = model
        self._controller = controller
        self._width = 400
        self._height = 200
        
        self.setWindowTitle('PyClick1.0')
        self.setFixedSize(self._width, self._height)
        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        self._ui.controlButton.clicked.connect(self._controller.clicker_status_control)
        
        self._model.counter_changed.connect(self.change_counter_clicks)
        self._model.time_changed.connect(self.change_counter_time)

    
    @pyqtSlot(int)
    def change_counter_clicks(self, value: int) -> None:
        self._ui.counterClicks.display(value)
    
    @pyqtSlot(float)
    def change_counter_time(self, value: float) -> None:
        self._ui.counterTime.display(value)
        