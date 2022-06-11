import evdev
import pyautogui
import time

from threading import Thread

class ClickerWorker(Thread):
    def __init__(
        self,
        counter_changed_signal, 
        time_changed_signal
    ) -> None:
        Thread.__init__(self, daemon=True)

        self._count = 0
        self._time = 0
        self._killed = False
        
        self._counter_changed_signal = counter_changed_signal
        self._time_changed_signal = time_changed_signal
        
    def run(self) -> None:
        while True:
            if self._killed:
                raise SystemExit()
            pyautogui.click()
            self.change_signals()    
    
    def change_signals(self) -> None:
        self._count += 1
        self._time += 0.1
        self._time_changed_signal.emit(self._time)
        self._counter_changed_signal.emit(self._count)
        
    def kill(self) -> None:
        self._killed = True


class KeyListenerWorker(Thread):
    def __init__(self, controller) -> None:
        Thread.__init__(self, daemon=True)
        
        self.device = evdev.InputDevice('/dev/input/event4')
        self.controller = controller
        self.limit = 0
        
    def run(self) -> None:
        for event in self.device.read_loop():
            self.limit += 1
            if self.limit == 1:
                self.controller.key_press_trigger(event.value)
            elif self.limit > 1:
                self.limit = 0