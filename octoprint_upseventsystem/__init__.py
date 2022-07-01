from __future__ import absolute_import
import octoprint.plugin
import octoprint.printer
import octoprint.printer.profile
import octoprint.util
import threading, time, datetime
from .EventSystem import *


# region Класс для сравнения времени
class Date:
	"""
	Класс даты
	"""

	def __init__(self, hour: int, minute: int) -> None:
		"""
		Инициализация класса даты
		\n
		:param hour: [int] => час
		:param minute: [int] => минута
		"""
		self.hour = hour
		self.minute = minute

	def __str__(self):
		return f"{self.hour}:{self.minute}"

	def __eq__(self, other):
		return (self.hour == other.hour and self.minute == other.minute)

	def __ge__(self, other):
		return self.__eq__(other) or self.__gt__(other)

	def __gt__(self, other):
		s_hour = self.hour
		if (self.hour == 0): s_hour = 24

		o_hour = other.hour
		if (other.hour == 0): o_hour = 24

		if (s_hour > o_hour):
			return True
		elif (s_hour == o_hour):
			return (self.minute > other.minute)

		return False
#endregion
#region Мусор
def Thread(func):
    """
    Декоратор Thread, для запуска функции в отдельном потоке
    """
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper
#endregion

class UpsEventSystemPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.BlueprintPlugin):
	def on_after_startup(self):
		print(EVENT_MANAGER.GetTriggerStr())

		fTrigger = EVENT_MANAGER.Append(TRIGGERS_DICT["ON_POWER_OFF"]({}))
		fTrigger.Connect(EVENTS_DICT["PT_LOG"]({"s": "POWER OFF!"}))

		sTrigger = EVENT_MANAGER.Append(TRIGGERS_DICT["ON_POWER_ON"]({}))
		sTrigger.Connect(EVENTS_DICT["PT_LOG"]({"s": "POWER ON!"}))

		print(EVENT_MANAGER.GetTriggerStr())
		print(EVENT_MANAGER.GetSettingsDict())

		self.updateTimer = octoprint.util.RepeatedTimer(0.25, self.Update)
		self.updateTimer.start()

	#region Манипуляции с потоками
	def on_shutdown(self):
		self._stopUpdateTimer()

	def _stopUpdateTimer(self):
		if (self.updateTimer != None):
			self.updateTimer.cancel()
	#endregion

	def Update(self) -> None:
		"""
		Вызов циклической функции раз в 5 секунд
		\n
		:return: None
		"""

		try:
			EVENT_MANAGER.Update()
			print("UPS is Alive!")
		except Exception as exception:
			print(exception)

	@octoprint.plugin.BlueprintPlugin.route("/get_triggers_list", methods=["GET"])
	def GetTriggersList(self):
		return EVENT_MANAGER.GetSettingsDict(), 200

	def get_settings_defaults(self):
		return {

		}

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=True)
		]

	def on_settings_save(self, data):
		self._logger.info(data)

		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

		self.currentSettings: dict = self._settings.settings.get(["plugins", "upseventsystem"], merged=True)

	def get_assets(self):
		return dict(
			js=["js/upseventsystem.js"],
			css=["css/upseventsystem.css"],
			less=["less/upseventsystem.less"]
		)

__plugin_name__ = "UPS EventSystem"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = UpsEventSystemPlugin()
