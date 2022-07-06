from .. import Event, Debug, PrinterManager

class PT_SAVE_TEMP(Event):
    def __init__(self, values: dict[str, str] = { }, id: str = None):
        self.defaultValues = { }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_SAVE_TEMP, self).__init__("PT_SAVE_TEMP", values, id)

    def Run(self) -> None:
        PrinterManager.SaveTemp()
        Debug.Success(Debug, f"Save temp with: {PrinterManager.SAVED_TEMP}", withDate=True)
