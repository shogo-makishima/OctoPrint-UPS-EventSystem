from __future__ import absolute_import
import octoprint.plugin
import octoprint.printer
import octoprint.printer.profile
import octoprint.util
import threading, time, datetime
from .EventSystem import *


class UpsEventSystemPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.BlueprintPlugin):
	def on_after_startup(self):
		Debug.LOGGER = self._logger
		PrinterManager.PRINTER = self._printer

		if (self._settings != None):
			settings = self._settings.settings.get(["plugins", "upseventsystem"], merged=True)

			self.ParseTriggers(settings)
			NUT_MANAGER.upsName = settings["currentUPS"]

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
			if (self._settings != None):
				NUT_MANAGER.UpdateUpsValues()
				EVENT_MANAGER.Update()
		except Exception as exception:
			Debug.Error(Debug, "ERROR")
			Debug.LOGGER.exception(exception)

	def ParseTriggers(self, data) -> None:
		"""
		Отпарсить словарь триггеров
		\n
		:param data: [dict] => словарь триггеров
		:return: None
		"""
		try:
			EVENT_MANAGER.GenerateFromList(data["customTriggers"])
			Debug.Success(Debug, "Parse new events has complete!")
		except Exception as exception:
			Debug.Error(Debug, "ERROR")
			Debug.LOGGER.exception()

	@octoprint.plugin.BlueprintPlugin.route("/get_triggers_list", methods=["GET"])
	def GetTriggersList(self):
		return EVENT_MANAGER.GetSettingsDict(), 200

	@octoprint.plugin.BlueprintPlugin.route("/get_custom_triggers_list", methods=["GET"])
	def GetCustomTriggersList(self):
		return self._settings.settings.get(["plugins", "upseventsystem"], merged=True), 200

	@octoprint.plugin.BlueprintPlugin.route("/get_ups_list", methods=["GET"])
	def GetUpsList(self):
		return { "ups": NUT_MANAGER.GetUpsList() }

	@octoprint.plugin.BlueprintPlugin.route("/get_current_battery_charge", methods=["GET"])
	def GetCurrentBatteryCharge(self):
		return { "charge" : NUT_MANAGER.GetBatteryCharge() }, 200

	def get_settings_defaults(self):
		NUT_MANAGER.UpdateUpsList()
		print(NUT_MANAGER.upsList)
		return {
			"customTriggers": [{}],
			"currentUPS": NUT_MANAGER.upsList[NUT_MANAGER.upsList.keys()[0]] if (len(NUT_MANAGER.upsList) > 0) else "none",
		}

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=True),
			dict(type="navbar", custom_bindings=True),
		]

	def on_settings_save(self, data):
		self._logger.info(data)

		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

		self.ParseTriggers(data)
		NUT_MANAGER.upsName = data["currentUPS"]

	def get_assets(self):
		return dict(
			js=["js/upseventsystem.js"],
			css=["css/upseventsystem.css"],
			less=["less/upseventsystem.less"]
		)


__plugin_name__ = "UPS EventSystem"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = UpsEventSystemPlugin()
