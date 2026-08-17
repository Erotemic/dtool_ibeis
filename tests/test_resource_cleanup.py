import gc
import sqlite3

import pytest


def test_testdata_depc_closes_sqlite_connections_when_collected():
    """Legacy doctest depcaches should not leak SQLite connections."""
    from dtool_ibeis.example_depcache import testdata_depc

    depc = testdata_depc(fname=':memory:')
    db = depc.fname_to_db[':memory:']
    connection = db.connection
    cleanup = depc._test_cleanup

    connection.execute('SELECT 1')
    assert cleanup.alive

    del depc
    gc.collect()

    assert not cleanup.alive
    with pytest.raises(sqlite3.ProgrammingError):
        connection.execute('SELECT 1')


def test_dtool_sqlite_connection_closes_on_collection():
    """Dtool's sqlite wrapper should not emit Python 3.13 ResourceWarning."""
    import warnings

    from dtool_ibeis import __SQLITE__ as lite

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always', ResourceWarning)
        connection = lite.connect(':memory:')
        connection.execute('SELECT 1')
        del connection

    resource_warnings = [
        item for item in caught if issubclass(item.category, ResourceWarning)
    ]
    assert resource_warnings == []


def test_dtool_sqlite_connection_preserves_explicit_factory():
    """Callers that provide a sqlite factory keep control of connection type."""
    import sqlite3

    from dtool_ibeis import __SQLITE__ as lite

    connection = lite.connect(':memory:', factory=sqlite3.Connection)
    try:
        assert type(connection) is sqlite3.Connection
    finally:
        connection.close()
