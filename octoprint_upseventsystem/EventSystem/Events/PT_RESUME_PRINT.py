from .. import Event, Debug, PrinterManager

class PT_RESUME_PRINT(Event):
    def __init__(self, values: dict[str, str] = {}, id: str = None):
        self.defaultValues = {}
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_RESUME_PRINT, self).__init__("PT_PAUSE_PRINT", values, id)

    def Run(self) -> None:
        Debug.Success(Debug, f"PRINTER: PAUSE!", withDate=True)
        PrinterManager.PRINTER.resume_print()
