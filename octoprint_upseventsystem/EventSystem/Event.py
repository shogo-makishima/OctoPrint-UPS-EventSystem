import random

LETTERS: str = """qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"""

def GenerateID(type: str = "T", length: int = 32) -> str:
    """
    Сгенерировать ID объекта
    \n
    :param type: [str] => тип объекта
    :param lenght: [int] => длинна ID
    :return: [str] => сгенерировать ID объекта
    """
    global LETTERS

    return type + ''.join(random.choice(LETTERS) for i in range(length))

class Event:
    """
    Класс события
    """
    def __init__(self, name: str = "PT_LOG", values: dict = { "x": "10" }, id: str = None) -> None:
        self.name = name
        """Имя события"""

        self.values = self.defaultValues | values
        """Переменные события"""

        self.ID = id if (id != None) else GenerateID("E", 32)
        """ID события"""

    def Run(self) -> None:
        """
        Выполнить событие по триггеру
        \n
        :return: None
        """
        pass

    def __str__(self) -> str:
        """
        Вернуть строку по классу
        \n
        :return: [str] => строка из класса
        """
        return name