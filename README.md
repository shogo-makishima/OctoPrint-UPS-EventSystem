# OctoPrint-UPS-EventSystem
### Плагин системы событий для ИБП и OctoPrint

# Список триггеров:

### ON_POWER_OFF
###### Срабатывет при отключении из сети

### ON_POWER_ON
###### Срабатывет при подключении к сети

### ON_CHARGE_CHANGE [charge] [mode]
###### Срабатывает при (зарядка|разрядке|полном заряде) батерии при достижении значения charge
#### charge [int] -> 0...100
###### Текущий заряд батареи [0, 100]
#### mode [str] -> FULLY_CHARGE | CHARGING | DISCHARGING
###### Текущий режим


# Список событий:

### PT_LOG [s]
###### Вывод строки в консоль
#### s [str] -> "Hello, World!"
###### Любая строка

### PT_SEND_GCODE [gcode] [state]
###### Отправка GCODE на принтер
#### gcode [str] -> "M115"
###### Строка GCODE
#### state [str] -> ANY | OPEN_SERIAL | DETECT_SERIAL | DETECT_BAUDRATE | CONNECTING | OPERATIONAL | PRINTING | PAUSED | CLOSED | ERROR | CLOSED_WITH_ERROR | TRANSFERING_FILE | OFFLINE | UNKNOWN | NONE
###### Nекущее состояние принтера
