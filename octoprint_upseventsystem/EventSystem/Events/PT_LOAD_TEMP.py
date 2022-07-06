from .. import Event, Debug, PrinterManager

class PT_LOAD_TEMP(Event):
    def __init__(self, values: dict[str, str] = { }, id: str = None):
        self.defaultValues = { }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_LOAD_TEMP, self).__init__("PT_LOAD_TEMP", values, id)

    def Run(self) -> None:
        if (PrinterManager.SAVED_TEMP == {}):
            Debug.Warning(Debug, "SAVED_TEMP is empty!", withDate=True)
            return

        """{'tool0': {'actual': 21.3, 'target': 0.0, 'offset': 0}, 'bed': {'actual': 21.3, 'target': 0.0, 'offset': 0}, 'chamber': {'actual': None, 'target': None, 'offset': 0}}"""

        if ("bed" in PrinterManager.SAVED_TEMP.keys()):
            PrinterManager.PRINTER.commands(f"M190 S{PrinterManager.SAVED_TEMP['bed']['target']}")

        tools = list(filter(lambda x: "tool" in x, PrinterManager.SAVED_TEMP.keys()))
        Debug.Message(Debug, f"Tools list: {tools}", withDate=True)
        for tool in tools:
            PrinterManager.PRINTER.commands(f"M109 {tool.replace('tool', 'T')} S{PrinterManager.SAVED_TEMP[tool]['target']}")

        Debug.Success(Debug, f"Load temp has complete with: {PrinterManager.SAVED_TEMP}", withDate=True)

        PrinterManager.SAVED_TEMP.clear()
