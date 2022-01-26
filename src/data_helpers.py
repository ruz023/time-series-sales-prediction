from typing import *

import pandas as pd


def load_lookup_tables(loc_table_fpath: str, 
                       dept_table_fpath: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """ Helper function for loading look-up tables"""
    loc_table = pd.read_csv(loc_table_fpath, dtype={"LOC_ID": int}, sep="|")
    dept_table = pd.read_csv(dept_table_fpath, dtype={"DEPT_ID": int}, sep="|")
    return loc_table, dept_table
