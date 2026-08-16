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
    'repr2',
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


def test_internal_column_attr_lookup_preserves_missing_key_defaults():
    """Mirror the missing-key behavior of ``ut.dict_take_column``."""
    from dtool_ibeis.depcache_table import _TableGeneralHelper

    data_col = {'intern_colname': 'value', 'isdata': True}
    extra_col = {'intern_colname': 'parent_rowid', 'isextra': True}

    class DummyTable(_TableGeneralHelper):
        internal_col_attrs = [data_col, extra_col]

    table = DummyTable()
    assert table.get_intern_col_attr('isdata') == [True, None]
    assert table.internal_data_col_attrs == [data_col]
