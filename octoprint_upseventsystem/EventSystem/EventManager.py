import jsonpickle

from . import Trigger, Event
from . import TRIGGERS_DICT, EVENTS_DICT


class EventManager:
    """
    Менеджер событий
    """
    def __init__(self) -> None:
        self.listTriggers: [Trigger] = []
        """Список триггеров"""

    def Update(self) -> None:
        """
        Функция обновления для проверки триггеров
        \n
        :return: None
        """
        for trigger in self.listTriggers:
            trigger.Update()

    def Append(self, trigger: Trigger) -> Trigger:
        """
        Добавить триггер в список и вернуть его
        \n
        :param trigger: [Trigger] => триггер системы событий
        :return: [Trigger] => триггер системы событий
        """
        self.listTriggers.append(trigger)
        return trigger

    def GetTriggerStr(self) -> list:
        """
        Получить список текущих событий
        \n
        :return: [list] => список текущих событий
        """
        return jsonpickle.encode(self.listTriggers)

    def GetSettingsDict(self) -> dict:
        """
        Вернуть словарь со всеми триггерами и событиями
        \n
        :return: [dict] => словарь со всеми триггерами и событиями
        """
        r_dict: dict = {
            "triggers": [],
            "events": [],
        }

        for triggerName in TRIGGERS_DICT.keys():
            defaultValues = TRIGGERS_DICT[triggerName]().defaultValues
            r_dict["triggers"].append({
                "name": triggerName,
                "values": [{ "name": key, "value": defaultValues[key]} for key in defaultValues.keys()],
            })

        for eventName in EVENTS_DICT.keys():
            defaultValues = EVENTS_DICT[eventName]().defaultValues
            r_dict["events"].append({
                "name": eventName,
                "values": [{ "name": key, "value": defaultValues[key]} for key in defaultValues.keys()],
            })

        return r_dict

    def __str__(self) -> str:
        """
        Вернуть строку по классу
        \n
        :return: [str] => строка из класса
        """
        t_str: str = ""

        for trigger in self.listTriggers:
            t_str += f"{str(trigger)}\n"

        return t_str


EVENT_MANAGER: EventManager = EventManager()
