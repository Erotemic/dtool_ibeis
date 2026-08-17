import gc
import sqlite3

import pytest


def test_testdata_depc_database_survives_temporary_owner_collection():
    """Escaping a DB from a temporary depcache must not close it."""
    from dtool_ibeis.example_depcache import testdata_depc

    db = testdata_depc(fname=':memory:')['notch'].db
    try:
        # This mirrors doctests such as ``db = testdata_depc()['notch'].db``.
        # Collect the temporary DependencyCache aggressively; the escaped DB
        # must remain live until its own owner closes it explicitly.
        gc.collect()
        db.connection.execute('SELECT 1')
        metadata_items = db.get_metadata_items()
        assert metadata_items
    finally:
        db.close()


def test_testdata_depc_explicit_close_closes_sqlite_connection():
    """The owning DependencyCache provides deterministic DB cleanup."""
    from dtool_ibeis.example_depcache import testdata_depc

    depc = testdata_depc(fname=':memory:')
    db = depc.fname_to_db[':memory:']
    connection = db.connection

    connection.execute('SELECT 1')
    depc.close()

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
