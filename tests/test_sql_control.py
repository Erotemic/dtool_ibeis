import pytest

from dtool_ibeis.sql_control import SQLDatabaseController


def test_make_add_table_rejects_missing_columns():
    db = SQLDatabaseController(fpath=':memory:')
    try:
        with pytest.raises(AssertionError, match='not given any columns'):
            db._make_add_table_sqlstr('empty_table', None)
    finally:
        db.close()
