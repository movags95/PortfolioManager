import sqlite3
from config import DB_PATH
conn = sqlite3.connect(DB_PATH)

def validate_connection(db_conn=conn):
    if not isinstance(db_conn, sqlite3.Connection):
        raise TypeError("Input must be a sqlite3.Connection object")

validate_connection(conn)

def execute(sql_stmt, values=None, db_conn=conn):
    c = db_conn.cursor()
    if values is None:
        c.execute(sql_stmt)
    else:
        c.execute(sql_stmt, values)

    return c.fetchall()

def commit(db_conn=conn):
    db_conn.commit()
    db_conn.close()






def get_asset_types():
    return execute('SELECT * FROM asset_types')

def get_assets():
    return execute('SELECT * FROM assets')

def get_transactions():
    return execute('SELECT * FROM transactions')

def get_asset_type_id_for(type):
    type = type.capitalize()
    types = get_asset_types()
    for row in types:
        if type in row:
            return row[0]

def get_asset_id_for(symbol):
    symbol = symbol.capitalize()
    assets = get_assets()
    for row in assets:
        if symbol in row:
            return row[0]

def insert_into_asset_types(asset_type):
    asset_type = asset_type.capitalize()
    execute('INSERT INTO asset_types (type) VALUES (?)', (asset_type,))
    commit()

def insert_into_assets(symbol, asset_type):
    symbol = symbol.upper()
    asset_type = asset_type.capitalize()
    asset_type_id = get_asset_type_id_for(asset_type)
    execute('INSERT INTO assets (symbol, asset_type_id) VALUES (?,?)', (symbol, asset_type_id,))
    commit()

def insert_into_transactions(symbol, price, qty, currency='GBP'):
    symbol = symbol.upper()
    currency = currency.upper()
    asset_id = get_asset_id_for(symbol)
    execute('INSERT INTO transactions (asset_id, purchase_currency, purchase_price, quantity) VALUES (?,?,?,?)',
            (asset_id, currency, price, qty,)
            )
    commit()





    

