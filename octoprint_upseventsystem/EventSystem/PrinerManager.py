class PrinterManager:
    """Класс для управления принетров"""
    PRINTER = None
    """Текущий принтер"""
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