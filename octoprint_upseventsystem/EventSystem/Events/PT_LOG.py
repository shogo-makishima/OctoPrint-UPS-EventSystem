from .. import Event, Debug

class PT_LOG(Event):
    def __init__(self, values: dict = { "value" : "10" }, id: str = None):
        self.defaultValues = {
            "s": "Hello, World!",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_LOG, self).__init__("PT_LOG", values, id)

    def Run(self) -> None:
        Debug.Message(Debug, *[self.values[key] for key in self.values.keys()], withDate=True)