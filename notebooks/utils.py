__all__ = ['logs', 'DEBUG', 'INFO', 'WARN', 'logging', 'rollback']

import logging
import sys
from contextlib import contextmanager

from sqlalchemy import Connection

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


@contextmanager
def rollback(con: Connection):
    """Creates a transaction that which revers changes upon completion."""
    with con.begin() as transaction:
        yield
        transaction.rollback()
