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
