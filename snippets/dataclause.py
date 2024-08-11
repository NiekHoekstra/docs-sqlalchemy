"""Provides helpers that allow data to be treated like a select statement."""

__all__ = ["select_union", "select_derived_table", "data_as_select"]

import functools
from typing import Any, Mapping, Sequence

from sqlalchemy import (
    ColumnClause,
    CompoundSelect,
    Dialect,
    RowMapping,
    Select,
    literal,
    select,
    values,
)

DictLike = Mapping[str, Any] | RowMapping


def select_union(rows: Sequence[DictLike], *columns: ColumnClause) -> CompoundSelect:
    """
    Create a "Derived Table", a Table Value construct.
    :param rows: Rows to embed.
    :param columns: Column definitions.
    :returns: CompoundSelect (union select) of values.
    :raises KeyError: A column is not found in one of the row mappings.
    """
    as_data: list[tuple] = [
        tuple(literal(r[c.key]).label(c.key) for c in columns) for r in rows
    ]
    # each row becomes its own select statement
    as_stmt = (select(*e) for e in as_data)
    # noinspection PyTypeChecker
    return functools.reduce(lambda a, b: a.union(b), as_stmt)


def select_derived_table(rows: Sequence[DictLike], *columns: ColumnClause) -> Select:
    """
    Create a "Derived Table", a Table Value construct.
    :param rows: Rows to use.
    :param columns: Column definitions.
    :returns: Select statement (SELECT ... FROM values ...).
    :raises KeyError: A column is not found in one of the row mappings.
    """
    as_data: list[tuple] = [
        tuple(literal(r[c.key], type_=c.type) for c in columns) for r in rows
    ]
    return select(values(*columns).data(as_data))


def data_as_select(
    rows: Sequence[DictLike], *columns: ColumnClause, dialect: Dialect | None = None
) -> CompoundSelect | Select:
    """
    Treat data as a select-like statement.
    This allows for more complex server-side actions by enabling the
    client to send data in a table-like structure, and using it in
    joins, updates, and inserts more easily.
    :param rows: Rows to use.
    :param columns: Column definitions.
    :param dialect: Dialect, used for optimization.
    :returns: Select-like statement.
    :raises KeyError: A column is not found in one of the row mappings.
    """
    if dialect is not None and dialect.name in ("snowflake", "mssql"):
        return select_derived_table(rows, *columns)
    return select_union(rows, *columns)


# from sqlalchemy.dialects.mssql import dialect as MSSQL
# x = select_union([
#     {'name': 'Jack', 'id': uuid4()}
# ], column('name', String), column('id', UUID))
# print(x.compile(dialect=MSSQL(), compile_kwargs={"literal_binds": True}))
