from .. import Trigger, Event
from .. import NUT_MANAGER
from random import randint

class ON_RANDOM_INT(Trigger):
    def __init__(self, values: dict[str, str] = { "value" : "10", "min" : "0", "max": "10" }):
        self.defaultValues = {
            "value" : "10",
            "min" : "0",
            "max": "10"
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(ON_RANDOM_INT, self).__init__("ON_RANDOM_INT", values)

    def Check(self) -> bool:
        """
        Проверка рандомного числа
        \n
        :return: [bool] => совпадает ли число с рандомным
        """
        intRandom: int = randint(int(self.values["min"]), int(self.values["max"]))
        return intRandom == int(self.values["value"])