from .. import Trigger, Event
from .. import NUT_MANAGER, PrinterManager, Debug
from random import randint

class ON_PRINTER_CHANGE_STATE(Trigger):
    def __init__(self, values: dict = { }, id: str = None):
        self.defaultValues = {
            "stateFrom" : "ANY",
            "stateTo" : "PRINTING"
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(ON_PRINTER_CHANGE_STATE, self).__init__("ON_PRINTER_CHANGE_STATE", values, id)

        self.lastState: str = "NONE"
        """Последнее состояние принтера"""

    def Check(self) -> bool:
        b_ret: bool = False

        stateFrom = self.values["stateFrom"]
        stateTo = self.values["stateTo"]

        stateCurrent = PrinterManager.PRINTER.get_state_id()

        if (stateFrom == "ANY"):
            b_ret = stateCurrent == stateTo
        else:
            b_ret = stateFrom == self.lastState and stateCurrent == stateTo

        self.lastState = stateCurrent
        return b_ret