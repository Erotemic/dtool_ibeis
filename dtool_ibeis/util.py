"""
import liberator
lib = liberator.Liberator()
import vtool_ibeis as vt
lib.add_dynamic(vt.to_undirected_edges)
lib.add_dynamic(vt.compute_unique_data_ids)
lib.close('vtool_ibeis')
print(lib.current_sourcecode())
"""
import numpy as np
import ubelt as ub


def to_undirected_edges(directed_edges, upper=False):
    assert len(directed_edges.shape) == 2 and directed_edges.shape[1] == 2
    #flipped = qaid_arr < daid_arr
    if upper:
        flipped = directed_edges.T[0] > directed_edges.T[1]
    else:
        flipped = directed_edges.T[0] < directed_edges.T[1]
    # standardize edge order
    edges_dupl = directed_edges.copy()
    edges_dupl[flipped, 0:2] = edges_dupl[flipped, 0:2][:, ::-1]
    undirected_edges = edges_dupl
    return undirected_edges


def compute_unique_data_ids_(hashable_rows, iddict_=None):
    if iddict_ is None:
        iddict_ = {}
    for row in hashable_rows:
        if row not in iddict_:
            iddict_[row] = len(iddict_)
    dataid_list = list(ub.take(iddict_, hashable_rows))
    return dataid_list


def compute_unique_data_ids(data):
    """
    This is actually faster than compute_unique_integer_data_ids it seems

    Example:
        >>> # ENABLE_DOCTEST
        >>> data = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [0, 0], [.534, .432], [.534, .432], [1, 0], [0, 1]])
        >>> dataid_list = compute_unique_data_ids(data)
        >>> result = 'dataid_list = ' + ub.repr2(dataid_list, with_dtype=True)
        >>> print(result)
        dataid_list = np.array([0, 1, 2, 3, 0, 4, 4, 2, 1], dtype=np.int32)
    """
    # construct a unique id for every edge
    hashable_rows = [tuple(row_.tolist()) for row_ in data]
    dataid_list = np.array(compute_unique_data_ids_(hashable_rows), dtype=np.int32)
    return dataid_list
