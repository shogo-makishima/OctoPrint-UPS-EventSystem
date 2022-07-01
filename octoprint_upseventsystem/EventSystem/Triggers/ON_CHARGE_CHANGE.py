from .. import Trigger, Event
from .. import NUT_MANAGER
from random import randint

class ON_CHARGE_CHANGE(Trigger):
    def __init__(self, values: dict[str, str] = { }):
        self.defaultValues = {
            # Заряд, при котором сбработает трриггер
            "charge": "99",
            # Три стадии:
            # 0: FULLY_CHARGE
            # 1: CHARGING
            # 2: DISCHARGING
            "mode": "DISCHARGING",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(ON_CHARGE_CHANGE, self).__init__("ON_CHARGE_CHANGE", values)

        self.b_isCalling: bool = False
        """Последний входящий показаетль заряда"""

    def Check(self) -> bool:
        b_ret: bool = False

        mode: str = str(self.values["mode"])
        charge: int = int(self.values["charge"])

        if (not self.b_isCalling and NUT_MANAGER.states[mode]):
            b_ret: bool = NUT_MANAGER.GetBatteryCharge() == charge if (mode != "FULLY_CHARGE") else NUT_MANAGER.states[mode]
            self.b_isCalling = b_ret
        elif ((mode != "FULLY_CHARGE") and charge != NUT_MANAGER.GetBatteryCharge()): self.b_isCalling = False
        elif ((mode == "FULLY_CHARGE") and not NUT_MANAGER.states[mode]): self.b_isCalling = False

        return b_ret