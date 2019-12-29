
"""
https://www.sqlite.org/download.html

cd ~/tmp
wget https://www.sqlite.org/2016/sqlite-amalgamation-3140200.zip
7z x sqlite-*.zip
"""
import sqlite3 as lite
from concurrent import futures
import utool as ut
import math

fpath = 'temp.sqlite3'
connection = lite.connect(fpath, detect_types=lite.PARSE_DECLTYPES, check_same_thread=False)
cur = connection.cursor()
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS table1 (
        col1 INTEGER,
        col2 INTEGER
    )
    ''')

with ut.Timer('INSERT'):
    niters = 300000
    for idx in ut.ProgIter(range(niters), 'insert'):
        import random
        col1 = random.randint(0, 1000)
        col2 = random.randint(0, 1000)

        cur.execute(
            '''
            INSERT INTO table1(rowid, col1, col2) VALUES (NULL, ?, ?)
            ''', (col1, col2))


with ut.Timer('SERIAL SELECT'):
    data = []
    rowid_list = list(range(1, niters + 1))
    for rowid in rowid_list:
        cur.execute('SELECT col1, col2 from table1 WHERE rowid=?', (rowid,))
        data.append(cur.fetchone())


def worker(args):
    import os
    fd = os.open(fpath, os.O_RDONLY)
    uri = '/dev/fd/%d' % fd
    connection = lite.connect(uri, detect_types=lite.PARSE_DECLTYPES)
    os.close(fd)

    connection = lite.connect(fpath, detect_types=lite.PARSE_DECLTYPES, check_same_thread=False)
    cur_ = connection.cursor()
    #cur_ = cur
    #cur = connection.cursor()
    data = []
    for rowid in args:
        cur_.execute('SELECT col1, col2 from table1 WHERE rowid=?', (rowid,))
        data.append(cur_.fetchone())
    return data


with ut.Timer('PARALLEL SELECT'):
    nprocs = 6
    #executor = futures.ThreadPoolExecutor(nprocs)
    executor = futures.ProcessPoolExecutor(nprocs)

    chunksize = int(math.ceil(len(rowid_list) / nprocs))
    args_list = [
        rowid_list[chunksize * i:chunksize * (i + 1)]
        for i in range(nprocs)
    ]

    fs_list = [executor.submit(worker, args) for args in args_list]

    result_list = [fs.result() for fs in ut.ProgIter(fs_list, lbl='fs')]

    result = ut.flatten(result_list)
    executor.shutdown(wait=False)


if False:
    # debug
    cur.execute('PRAGMA TABLE_INFO(table1)')
    cur.fetchall()
    cur.execute('PRAGMA compile_options')
    cur.fetchall()


#SELECT * FROM <TABLE NAME> WHERE rowid IN (SELECT rowid FROM <TEMP TABLE> WHERE flag=1)
