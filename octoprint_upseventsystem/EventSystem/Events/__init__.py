from .. import Event

from .PT_LOG import PT_LOG
from .PT_ERROR import PT_ERROR

EVENTS_DICT: dict[str, Event] = {
    "PT_LOG": PT_LOG,
    "PT_ERROR": PT_ERROR,
}
