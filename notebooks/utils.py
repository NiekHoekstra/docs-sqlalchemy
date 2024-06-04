__all__ = ['logs', 'DEBUG', 'INFO', 'WARN', 'logging']

from contextlib import contextmanager
import logging
import sys

WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARN)

logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


@contextmanager
def logs(level=logging.INFO):
    state = handler.level
    handler.setLevel(level)
    try:
        yield
    finally:
        handler.setLevel(state)
