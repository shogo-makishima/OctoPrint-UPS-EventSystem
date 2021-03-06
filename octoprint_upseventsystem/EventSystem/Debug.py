from datetime import datetime
import logging, pathlib, shutil, os

class ByteType:
    def __init__(self, code = "\33[0m"): self.code = code
    def __str__(self): return self.code

class Colored:
    TEXT_RED = ByteType("\33[31m")
    TEXT_YELLOW = ByteType("\33[93m")
    TEXT_GREEN = ByteType("\33[92m")
    TEXT_ITALIC = ByteType("\33[3m")
    TEXT_BOLD = ByteType("\33[1m")
    TEXT_STANDART = ByteType("\33[0m")
    TEXT_BLINK = ByteType("\33[94m")

class Debug:
    LOGGER = None

    def Message(self, object: object = "MESSAGE", withDate: bool = True):
        self.LOGGER.info(f"{Colored.TEXT_BOLD}{Colored.TEXT_BLINK}{Colored.TEXT_ITALIC}{datetime.now().strftime('[%Y.%m.%d %H:%M:%S] -->') if (withDate) else ''} MESSAGE: {Colored.TEXT_STANDART}{object.__str__()}")

    def Success(self, object: object = "SUCCESS", withDate: bool = True):
        self.LOGGER.info(f"{Colored.TEXT_BOLD}{Colored.TEXT_GREEN}{Colored.TEXT_ITALIC}{datetime.now().strftime('[%Y.%m.%d %H:%M:%S] -->') if (withDate) else ''} SUCCESS: {Colored.TEXT_STANDART}{object.__str__()}")

    def Warning(self, object: object = "WARNING", withDate: bool = True):
        self.LOGGER.info(f"{Colored.TEXT_BOLD}{Colored.TEXT_YELLOW}{Colored.TEXT_ITALIC}{datetime.now().strftime('[%Y.%m.%d %H:%M:%S] -->') if (withDate) else ''} WARNING: {Colored.TEXT_STANDART}{object.__str__()}")

    def Error(self, object: object = "ERROR", withDate: bool = True):
        self.LOGGER.info(f"{Colored.TEXT_BOLD}{Colored.TEXT_RED}{Colored.TEXT_ITALIC}{datetime.now().strftime('[%Y.%m.%d %H:%M:%S] -->') if (withDate) else ''} ERROR: {Colored.TEXT_STANDART}{object.__str__()}")