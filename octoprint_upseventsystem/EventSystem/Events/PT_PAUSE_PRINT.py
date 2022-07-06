from .. import Event, Debug, PrinterManager

class PT_PAUSE_PRINT(Event):
    def __init__(self, values: dict = {}, id: str = None):
        self.defaultValues = {}
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_PAUSE_PRINT, self).__init__("PT_PAUSE_PRINT", values, id)

    def Run(self) -> None:
        Debug.Success(Debug, f"PRINTER: PAUSE!", withDate=True)
        PrinterManager.PRINTER.pause_print()

