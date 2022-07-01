from .. import Event

class PT_LOG(Event):
    def __init__(self, values: dict[str, str] = { "value" : "10" }):
        self.defaultValues = {
            "s": "Hello, World!",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_LOG, self).__init__("PT_LOG", values)

    def Run(self) -> None:
        print(*[self.values[key]  for key in self.values.keys()])