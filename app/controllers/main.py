import evdev

from PyQt6.QtCore import QObject
from PyQt6.QtCore import Qt

from app.model.main import Model
from app.worker import KeyListenerWorker


class Controller(QObject):
    def __init__(self, model: Model) -> None:
        super().__init__()
        
        self._model = model
        
        self.setup_key_listener()
    
    def clicker_status_control(self) -> None:
        self._model.clicker_status = not self._model.clicker_status
    
    def key_press_trigger(self, key) -> None:
        match key:
            case evdev.ecodes.KEY_F2:
                self.clicker_status_control()
    
    def setup_key_listener(self) -> None:
        key_listener = KeyListenerWorker(self)
        key_listener.start()