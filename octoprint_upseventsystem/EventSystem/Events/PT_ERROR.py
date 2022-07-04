from .. import Event, Debug

class PT_ERROR(Event):
    def __init__(self, values: dict[str, str] = { "value" : "10" }, id: str = None):
        self.defaultValues = {
            "s": "Hello, World!",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_ERROR, self).__init__("PT_LOG", values, id)

    def Run(self) -> None:
        Debug.Error(Debug, *[self.values[key] for key in self.values.keys()], withDate=True)