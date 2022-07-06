from nut2 import PyNUTClient
from . import jsonpickle
import socket

DEBUG: bool = False
"""Использовать ли эмулятор NUT"""

if (DEBUG):
    import requests

class NutManager:
    """
    Менеджер ИБП
    """
    def __init__(self) -> None:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        print(hostname, IPAddr)

        self.CLIENT = PyNUTClient("0.0.0.0") if (not DEBUG) else None
        """Nut клиент"""

        self.upsList: list[str] = []
        """Список ИБП"""

        self.upsName: str = "cps-vector200-1"
        """Текущий ИБП"""

        self.upsValues: dict[str, str] = {}
        """Список переменных для ИБП"""

        self.states: dict[str, bool] = {
            "POWER_ON": True,
            "POWER_OFF": False,
            "CHARGING": True,
            "DISCHARGING": False,
            "FULLY_CHARGE": False,
        }
        """Текущее состояние блока питания"""

        self.__lastCharge: int = 100
        """Последний процент заряда ИБП"""

    def UpdateUpsValues(self) -> None:
        """
        Обновить состояние ИБП
        \n
        :return: None
        """
        self.upsValues = self.CLIENT.list_vars(self.upsName) if (not DEBUG) else requests.request("GET", "http://127.0.0.1:23336/get_ups_status").json()
        self.UpdateStates()

    def UpdateStates(self) -> None:
        """
        Обновить состояние ИБП
        \n
        :return: None
        """

        # OB [От батареи] OL [От шнура питания] DISCHRG [Разряд] CHRG [Заряд] LB [Малый заряд]
        status: str = self.upsValues["ups.status"]
        if (status.count(" ") > 0): status = status.split(" ")

        self.states["POWER_ON"] = "OL" in status
        self.states["POWER_OFF"] = "OB" in status

        self.states["CHARGING"] = "CHRG" in status
        self.states["DISCHARGING"] = "DISCHRG" in status
        self.states["FULLY_CHARGE"] = not self.states["CHARGING"] and not self.states["DISCHARGING"]

        """
        currentVoltage = self.GetInputVoltage()
        currentCharge = self.GetBatteryCharge()

        POWER_ON: bool = currentVoltage > int(self.upsValues["input.transfer.low"]) and currentVoltage < int(self.upsValues["input.transfer.high"])
        self.states["POWER_ON"] = POWER_ON
        self.states["POWER_OFF"] = not POWER_ON

        currentChargeEqual: bool = currentCharge != self.__lastCharge
        self.states["CHARGING"] = currentCharge > self.__lastCharge and currentChargeEqual
        self.states["DISCHARGING"] = currentCharge < self.__lastCharge and currentChargeEqual
        self.states["FULLY_CHARGE"] = currentCharge == 100
        

        self.__lastCharge = currentCharge
        """

    def GetBatteryCharge(self) -> int:
        """
        Получить зарядку батареи из текущего ИБП
        \n
        :return: [int] => текущий процент заряда
        """
        return int(self.upsValues["battery.charge"])

    def GetUpsList(self) -> list:
        """
        Получить список ИБП
        \n
        :return: [list] => список ибп
        """
        return [{ "name": ups } for ups in self.upsList]


    def GetInputVoltage(self) -> int:
        """
        Получить входящее в ИБП напряжение
        \n
        :return: [int] => входящее в ИБП напряжение
        """
        return float(self.upsValues["input.voltage"])

    def UpdateUpsList(self) -> None:
        """
        Обновить список ИБП
        \n
        :return: None
        """
        self.upsList = self.CLIENT.list_ups() if (not DEBUG) else ["test", "test1"]


NUT_MANAGER: NutManager = NutManager()
NUT_MANAGER.UpdateUpsList()
NUT_MANAGER.UpdateUpsValues()