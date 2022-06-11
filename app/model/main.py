from PyQt6.QtCore import QObject, pyqtSignal

from app.worker import ClickerWorker


class Model(QObject):
    counter_changed = pyqtSignal(int)
    time_changed = pyqtSignal(float)
    clicker_status = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

        self._clicker_status = False
        self._queue: list[ClickerWorker] = []
    
    @property
    def clicker_status(self) -> bool:
        return self._clicker_status

    @clicker_status.setter
    def clicker_status(self, value) -> None:
        self._clicker_status = value
        
        if self.clicker_status:
            clicker = ClickerWorker(self.counter_changed, self.time_changed)
            self._queue.append(clicker)
            clicker.start()
        else:
            clicker = self._queue.pop()
            clicker.kill()
            clicker.join()