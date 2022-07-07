class PrinterManager:
    """Класс для управления принетров"""
    PRINTER = None
    """Текущий принтер"""
    LAST_GCODE: dict = {
        "text": "M115",
        "fileline": "0",
    }
    """Последняя отправленная команда GCODE"""
    SAVED_TEMP: dict = { }
    """Сохраненная температура"""

    @staticmethod
    def SaveTemp() -> None:
        """
        Сохранить текущую температуру печати
        \n
        :return: None
        """
        PrinterManager.SAVED_TEMP = PrinterManager.PRINTER.get_current_temperatures()