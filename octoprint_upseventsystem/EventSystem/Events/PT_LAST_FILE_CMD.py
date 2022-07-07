from .. import Event, Debug, PrinterManager

class PT_LAST_FILE_CMD(Event):
    def __init__(self, values: dict = { }, id: str = None):
        self.defaultValues = { }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_LAST_FILE_CMD, self).__init__("PT_LAST_FILE_CMD", values, id)

    def Run(self) -> None:
        Debug.Warning(Debug, f"GCODE: {PrinterManager.LAST_GCODE}", withDate=True)