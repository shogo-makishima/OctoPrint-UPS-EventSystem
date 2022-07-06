from .. import Trigger, Event
from .. import NUT_MANAGER
from random import randint

class ON_POWER_ON(Trigger):
    def __init__(self, values: dict = { }, id: str = None):
        self.defaultValues = {}
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(ON_POWER_ON, self).__init__("ON_POWER_ON", values, id)

        self.lastInputState: bool = True
        """Последнее входящее напряжение"""

    def Check(self) -> bool:
        POWER_ON = NUT_MANAGER.states["POWER_ON"]
        b_ret: bool = self.lastInputState != POWER_ON and POWER_ON

        self.lastInputState = POWER_ON
        return b_ret