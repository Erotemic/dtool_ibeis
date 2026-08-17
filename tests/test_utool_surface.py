import ast
import re
from pathlib import Path


RETIRED_UTOOL_HELPERS = {
    'NiceRepr',
    'NoParam',
    'apply_grouping',
    'argsort',
    'assertpath',
    'augpath',
    'codeblock',
    'colorprint',
    'compress',
    'copy',
    'cprint',
    'ddict',
    'dict_hist',
    'dict_take',
    'dict_take_column',
    'ensuredir',
    'ensure_iterable',
    'ensure_unicode',
    'filter_Nones',
    'flag_None_items',
    'flag_not_None_items',
    'flag_unique_items',
    'flatten',
    'get_argflag',
    'get_list_column',
    'group_items',
    'identity',
    'indent',
    'index_complement',
    'invert_dict',
    'isiterable',
    'list_transpose',
    'lmap',
    'nx_node_dict',
    'nx_sink_nodes',
    'nx_source_nodes',
    'odict',
    'partial',
    'print_traceback',
    'product_nonsame',
    'readfrom',
    'setdiff',
    'take',
    'take_column',
    'unflat_take',
    'unique',
    'where',
    'writeto',
}


def _active_utool_attributes():
    root = Path(__file__).parents[1] / 'dtool_ibeis'
    found = set()
    for fpath in root.rglob('*.py'):
        tree = ast.parse(fpath.read_text(), filename=str(fpath))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id in {'ut', 'utool'}
            ):
                found.add(node.attr)
    return found


def test_retired_utool_convenience_helpers_stay_retired():
    active = _active_utool_attributes()
    regressions = sorted(active & RETIRED_UTOOL_HELPERS)
    assert not regressions, 'retired utool helpers reintroduced: {!r}'.format(regressions)


def test_direct_runtime_dependencies_are_declared():
    runtime_fpath = Path(__file__).parents[1] / 'requirements' / 'runtime.txt'
    declared = {
        re.split(r'[<>=!~;\s\[]', line.strip(), maxsplit=1)[0].lower()
        for line in runtime_fpath.read_text().splitlines()
        if line.strip() and not line.lstrip().startswith('#')
    }
    assert {'loguru', 'networkx', 'numpy', 'parse'} <= declared


def test_multi_parent_internal_data_columns_ignore_extra_metadata():
    """Exercise the metadata path used by ``DependencyCacheTable.delete_rows``.

    Multi-parent tables add an internal ``*_setsize`` column which is not a
    data column and therefore intentionally has no ``isdata`` key.  Attribute
    lookup must preserve the old ``dict_take_column`` missing-key semantics
    rather than raising ``KeyError``.
    """
    from dtool_ibeis.depcache_table import DependencyCacheTable

    table = DependencyCacheTable(
        depc=None,
        parent_tablenames=['images*'],
        tablename='thumbnails',
        data_colnames=['value'],
        data_coltypes=[int],
        preproc_func=None,
    )

    extra_cols = [row for row in table.internal_col_attrs if row.get('isextra')]
    assert len(extra_cols) == 1
    assert extra_cols[0]['intern_colname'] == 'images_setsize'
    assert 'isdata' not in extra_cols[0]

    # This is the first metadata lookup performed by delete_rows().  The IBEIS
    # regression failed here while deleting image thumbnails.
    assert table.get_intern_data_col_attr('intern_colname') == ['value']
    assert table.get_intern_data_col_attr('is_external_pointer') == [None]


def test_builtin_map_calls_do_not_receive_keyword_arguments():
    """Catch invalid mechanical conversions from helpers such as ``ut.lmap``."""
    root = Path(__file__).parents[1] / 'dtool_ibeis'
    bad_calls = []
    for fpath in root.rglob('*.py'):
        tree = ast.parse(fpath.read_text(), filename=str(fpath))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == 'map'
                and node.keywords
            ):
                bad_calls.append((str(fpath), node.lineno))
    assert not bad_calls, 'builtin map() cannot accept keywords: {!r}'.format(bad_calls)

