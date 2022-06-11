import sys

from PyQt6.QtWidgets import QApplication

from app.controllers.main import Controller
from app.model.main import Model
from app.views.main import View


class App(QApplication):
    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
        
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model, self.controller)
        self.view.show()


app = App(sys.argv)

sys.exit(app.exec())