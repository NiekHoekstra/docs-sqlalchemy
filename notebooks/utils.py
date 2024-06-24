__all__ = ['logs', 'DEBUG', 'INFO', 'WARN', 'logging', 'rollback']

import logging
import sys
from contextlib import contextmanager

from sqlalchemy import Connection, text

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


def try_fix_quirks(con: Connection):
    """Tries to fix any database specific quirks for testing."""
    if con.dialect.name == 'sqlite':
        # Enable enforcement of foreign keys (when using sqlite).
        with con.begin():
            con.execute(text('pragma foreign_keys=ON'))
