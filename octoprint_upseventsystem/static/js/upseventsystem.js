$(function() {
    // Символы для генерации ID
    const LETTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

    let TRIGGERS_LIST = [{}]
    let EVENTS_LIST = [{}]

    function findTriggerSettings(name) {
        for (let i = 0; i < TRIGGERS_LIST.length; i++) {
            if (TRIGGERS_LIST[i].name === name) return TRIGGERS_LIST[i];
        }

        return null;
    }

    function findEventSettings(name) {
        for (let i = 0; i < EVENTS_LIST.length; i++) {
            if (EVENTS_LIST[i].name === name) return EVENTS_LIST[i];
        }

        return null;
    }

    // Сгенерировать ID элемента
    function GenerateID(type, length) {
        let s_result = type;

        let lettersLength = LETTERS.length;

        for (let i = 0; i < lettersLength; i++ ) {
            s_result += LETTERS.charAt(Math.floor(Math.random() * lettersLength));
        }

        return s_result;
    }

    // Глубокая копия объекта
    function DeepCopy(object) {
        return JSON.parse(JSON.stringify(object));
    }

    Array.prototype.remove = function (object) {
        return this.filter(e => e !== object);
    }

    // Компонент события
    class SEvent {
        constructor(name, values, id = null) {
            if (id === null) {
                // Создание уникального ID
                this.sID = GenerateID("E", 32);
            } else {
                this.sID = id;
            }
            // Имя события для сохранения
            this.sName = name;
            // Переменные события для хранения
            this.sValues = DeepCopy(values);
            // ID события обозрева
            this.ID = ko.observable(this.sID);

            // Переменные события обозрева
            this.values = ko.observable(this.sValues);

            // Имя события обозрева
            this.name = ko.observable(this.sName);
            this.name.subscribe(function (newValue) {
                if (newValue === this.sName) return;

                console.log(newValue);

                this.sName = newValue;
                this.sValues = DeepCopy(findEventSettings(this.sName).values);
                this.values(this.sValues);

                console.log("CHANGED -> " + this.ID + " : " + this.sName + " : " + this.sValues);
            }, this);
        }
    }

    // Компонент триггера
    class STrigger {
        constructor(name, values, id = null) {
            if (id === null) {
                // Создание уникального ID
                this.sID = GenerateID("T", 32);
            } else {
                this.sID = id;
            }
            // Имя триггера для сохранения
            this.sName = name;
            // Переменные триггера для хранения
            this.sValues = DeepCopy(values);
            // События по триггеру
            this.sEvents = []

            // ID триггера обозрева
            this.ID = ko.observable(this.sID);

            // Переменные триггера обозрева
            this.values = ko.observable(this.sValues);

            // События триггера
            this.events = ko.observable(this.sEvents);

            // Имя триггера обозрева
            this.name = ko.observable(this.sName);
            this.name.subscribe(function (newValue) {
                if (newValue === this.sName) return;

                console.log(newValue);

                this.sName = newValue;
                console.log(TRIGGERS_LIST);
                console.log(JSON.stringify(findTriggerSettings(this.sName)));
                this.sValues = DeepCopy(findTriggerSettings(this.sName).values);
                this.sEvents = []

                this.values(this.sValues);
                this.events(this.sEvents);

                console.log("CHANGED -> " + this.ID + " : " + this.sName + " : " + this.sValues);
            }, this);
        }

        findEventByID(ID) {
            for (let i = 0; i < this.sEvents.length; i++) {
                if (this.sEvents[i].ID === ID) return this.sEvents[i];
            }

            return null;
        }

        removeEvent(ID) {
            let event = this.findEventByID(ID);
            console.log(JSON.stringify(event));
            console.log(JSON.stringify(this.sEvents));

            if (event !== null) {
                this.sEvents = this.sEvents.remove(event);
                console.log(this.sEvents)
                this.events(this.sEvents);
            }
        }

        pushEvent(event) {
            this.sEvents.push(event);
            this.events(this.sEvents);
        }

        addNewEvent(settingsEvents) {
            this.sEvents.push(new SEvent(settingsEvents()[0].name, settingsEvents()[0].values));
            this.events(this.sEvents);
        }
    }

    function UpsEventSystemViewModel(parameters) {
        const self = this;

        self.settings = parameters[0];

        // Локальный список триггеров
        self._triggersList = []

        // Список триггеров на экране
        self.customTriggers = ko.observableArray();

        // Список триггеров для Drop-Down'а
        self.settingsTriggers = ko.observable();

        // Список событий для Drop-Down'а
        self.settingsEvents = ko.observable();

        self.onBeforeBinding = function() {
            self.getTriggersList();
            self.getCustomTriggersList();
        }

        // Сохранить настройки
        self.saveData = function() {
            console.log(self.customTriggers());

            let data = {
                plugins: {
                    upseventsystem: {
                        customTriggers: self.customTriggers(),
                    }
                }
            };

			self.settings.saveData(data);
        }

        // Найти триггер по ID
        self.findTriggerById = function (ID) {
            return ko.utils.arrayFirst(self.customTriggers(), function (item) {
                return item.ID === ID;
            });
        }

        // Добавить новый триггер
        // : name : строка с название триггера
        self.addNewTrigger = function () {
            self.customTriggers.push(new STrigger(self.settingsTriggers()[0].name, self.settingsTriggers()[0].values));
        }

        // Удалить триггер по ID
        self.removeTrigger = function (ID) {
            let trigger = self.findTriggerById(ID);
            self.customTriggers.remove(trigger);
        }

        // Получить список триггеров и событий
        self.getTriggersList = function() {
            $.ajax({
                type: "GET",
                url: "plugin/upseventsystem/get_triggers_list",
                cache: false,
                dataType: "text/json",
                async: false,
                statusCode: {
                    200: function(data) {
                        let json = JSON.parse(data.responseText);

                        TRIGGERS_LIST = json["triggers"];
                        EVENTS_LIST = json["events"];

                        self.settingsTriggers(TRIGGERS_LIST);
                        self.settingsEvents(EVENTS_LIST);
                    }
                }
            });
        }

        // Получить список триггеров и событий
        self.getCustomTriggersList = function() {
            $.ajax({
                type: "GET",
                url: "plugin/upseventsystem/get_custom_triggers_list",
                cache: false,
                dataType: "text/json",
                async: false,
                statusCode: {
                    200: function(data) {
                        let triggersJson = JSON.parse(data.responseText)["customTriggers"];
                        console.log("TRIGGERS: " + JSON.stringify(triggersJson));

                        if (JSON.stringify(triggersJson) === "[{}]") return;

                        for (let i = 0; i < triggersJson.length; i++) {
                            let triggerJson = triggersJson[i];

                            let newTrigger = new STrigger(triggerJson.sName, triggerJson.sValues, triggerJson.sID);

                            for (let i = 0; i < triggerJson.sEvents.length; i++) {
                                let eventJson = triggerJson.sEvents[i];

                                let newEvent = new SEvent(eventJson.sName, eventJson.sValues, eventJson.sID);

                                newTrigger.pushEvent(newEvent);
                            }

                            self.customTriggers.push(newTrigger);

                        }
                    }
                }
            });
        }
    }

    // This is how our plugin registers itself with the application, by adding some configuration information to
    // the global variable ADDITIONAL_VIEWMODELS
    ADDITIONAL_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        UpsEventSystemViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request here is the order
        // in which the dependencies will be injected into your view model upon instantiation via the parameters
        // argument
        ["settingsViewModel"],

        // Finally, this is the list of all elements we want this view model to be bound to.
        // [document.getElementById("settings_plugin_upseventsystem")]
        ["#settings_plugin_upseventsystem"]
    ]);
});
