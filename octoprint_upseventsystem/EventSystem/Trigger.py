from . import Event, GenerateID, MergeDicts

class Trigger:
    """
    Класс триггера, который вызывает функцию события
    """
    def __init__(self, name: str = "ON_TIME_CHANGE", values: dict = { "x" : 10 }, id: str = None) -> None:
        self.name = name
        """Имя триггера"""

        self.events: list = []
        """Список присоединенных событий"""

        self.values = MergeDicts(self.defaultValues, values)
        """Список переменных для проверки состояния триггера"""

        self.id = id if (id != None) else GenerateID("T", 32)
        """ID Триггера"""

    def Update(self) -> None:
        """
        Функция обновления триггера
        \n
        :return: None
        """
        if (self.Check()): self.RunEvents()

    def Check(self) -> bool:
        """
        Проверить проходят ли условия вызова для триггера
        \n
        :return: [bool] => проходят ли условия вызова события
        """
        pass

    def Connect(self, event: Event) -> None:
        """
        Присоеденить событие к триггеру
        \n
        :param event: [Event] => событие
        :return: None
        """
        self.events.append(event)

    def RunEvents(self) -> None:
        """
        Вызов всех событий по триггеру
        \n
        :return: None
        """
        for event in self.events:
            event.Run()

    def __str__(self) -> str:
        """
        Вернуть строку по классу
        \n
        :return: [str] => строка из класса
        """
        return f"{self.name} : {self.values}"