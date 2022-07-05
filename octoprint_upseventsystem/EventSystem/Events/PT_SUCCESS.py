from .. import Event, Debug

class PT_SUCCESS(Event):
    def __init__(self, values: dict[str, str] = { "s" : "10" }, id: str = None):
        self.defaultValues = {
            "s": "Hello, World!",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_SUCCESS, self).__init__("PT_SUCCESS", values, id)

    def Run(self) -> None:
        Debug.Success(Debug, *[self.values[key] for key in self.values.keys()], withDate=True)