from .. import Event, Debug

class PT_WARNING(Event):
    def __init__(self, values: dict[str, str] = { "s" : "Hello, World!" }, id: str = None):
        self.defaultValues = {
            "s": "Hello, World!",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_WARNING, self).__init__("PT_WARNING", values, id)

    def Run(self) -> None:
        Debug.Warning(Debug, *[self.values[key] for key in self.values.keys()], withDate=True)