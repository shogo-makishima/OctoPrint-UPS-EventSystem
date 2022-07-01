from .. import Trigger

from .ON_RANDOM_INT import ON_RANDOM_INT
from .ON_POWER_OFF import ON_POWER_OFF
from .ON_POWER_ON import ON_POWER_ON
from .ON_CHARGE_CHANGE import ON_CHARGE_CHANGE

TRIGGERS_DICT: dict[str, Trigger] = {
    "ON_RANDOM_INT": ON_RANDOM_INT,
    "ON_POWER_OFF": ON_POWER_OFF,
    "ON_POWER_ON": ON_POWER_ON,
    "ON_CHARGE_CHANGE": ON_CHARGE_CHANGE,
}
