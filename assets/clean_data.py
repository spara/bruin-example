"""@bruin
name: gsheet.engineers
connection: duckdb-default

materialization:
    type: table
    strategy: merge

columns:
    - name: _dlt_id
      primary_key: true
    - name: name
    - name: networking_through
    - name: position
    - name: _dlt_load_id
    - name: contact_date
@bruin"""

import pandas as pd
import duckdb as dd

def clean(value):
    if 'linked'.casefold() in value.casefold():
        return 'Linkedin'
    else: 
        return 'Mutual Friend'

def materialize():
    con = dd.connect('bruin.db')
    df = con.execute('SELECT * FROM gsheet.engineers;').df()
    networking = df['networking_through']
    df['networking_through'] = networking.apply(clean)

    return df