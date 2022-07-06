from .. import Trigger, Event
from .. import NUT_MANAGER
from random import randint

class ON_POWER_OFF(Trigger):
    def __init__(self, values: dict = { }, id: str = None):
        self.defaultValues = {}
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(ON_POWER_OFF, self).__init__("ON_POWER_OFF", values, id)

        self.lastInputState: bool = True
        """Последнее входящее напряжение"""

    def Check(self) -> bool:
        POWER_OFF = NUT_MANAGER.states["POWER_OFF"]
        b_ret: bool = self.lastInputState != POWER_OFF and POWER_OFF

        self.lastInputState = POWER_OFF
        return b_ret