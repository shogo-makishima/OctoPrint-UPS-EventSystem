from .. import Event, Debug, PrinterManager

class PT_SEND_GCODE(Event):
    def __init__(self, values: dict = { "gcode" : "M115" }, id: str = None):
        self.defaultValues = {
            "gcode": "M115",
            "state": "ANY",
        }
        """ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР! Базовые переменные!"""

        super(PT_SEND_GCODE, self).__init__("PT_SEND_GCODE", values, id)

    def Run(self) -> None:
        if (self.values["state"] == "ANY" or PrinterManager.PRINTER.get_state_id() == self.values["state"]):
            gcodeToSend: str = [' '.join(i.split()) for i in self.values["gcode"].split(",")]
            Debug.Success(Debug, f"GCODE: {gcodeToSend}", withDate=True)
            PrinterManager.PRINTER.commands(gcodeToSend)
        else:
            Debug.Warning(Debug, f"{self.values['state']} is False!")