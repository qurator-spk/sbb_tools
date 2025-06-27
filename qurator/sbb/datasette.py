import numpy as np
import pandas as pd
from tqdm import tqdm as tqdm
import click
from collections import Counter
import os
import sqlite3
from qurator.utils.parallel import run as prun


@click.command()
@click.argument('fulltext-sqlite', type=click.Path(exists=True), required=True, nargs=1)
@click.argument('mods-info-csv', type=click.Path(exists=True), required=True, nargs=1)
def setup_datasette_fulltext(fulltext_sqlite, mods_info_csv):

    mods_info = pd.read_csv(mods_info_csv).reset_index(drop=True)

    with sqlite3.connect(fulltext_sqlite) as con:

        con.execute("UPDATE text SET ppn = 'PPN' || ppn WHERE ppn NOT GLOB 'PPN*'")

        mods_info.to_sql('mods_info', con=con, if_exists='replace', index=False)

        con.execute('CREATE INDEX IF NOT EXISTS idx_ppn_mods_info ON mods_info(ppn)')

        con.execute('CREATE VIEW text_with_location (rowid, ppn, file, title, text, latitude, longitude) '
                    'AS SELECT '
                    'text.rowid, text.ppn, text.file_name, mods_info.titleInfo_title, text.text, '
                    'mods_info.latitude, mods_info.longitude FROM text join mods_info on mods_info.ppn=text.ppn')

        con.execute('CREATE VIRTUAL TABLE "text_with_location_fts" USING FTS5 (text, content="text_with_location")')

        con.execute('INSERT INTO "text_with_location_fts" (rowid, text) SELECT rowid, text FROM text_with_location_fts')

        # =======

        con.execute('CREATE VIRTUAL TABLE "text_fts" USING FTS5 (text, content="text")')

        con.execute('INSERT INTO "text_fts" (rowid, text) SELECT rowid, text FROM text')

        # =======



