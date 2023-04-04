def get_asset_types(cursor):
    cursor.execute('SELECT * FROM asset_types')
    return cursor.fetchall()

def get_assets(cursor):
    cursor.execute('SELECT * FROM assets')
    return cursor.fetchall()

def get_transactions(cursor):
    cursor.execute('SELECT * FROM transactions')
    return cursor.fetchall()

def get_asset_type_id_for(cursor, type):
    type = type.capitalize()
    types = get_asset_types(cursor)
    for row in types:
        if type in row:
            return row[0]

def get_asset_id_for(cursor, symbol=None, asset_type_id=None):
    # This will run when the function is supplied with an asset_type_id and will return a tuple of values
    if asset_type_id != None:
        asset_ids = []
        assets = get_assets(c)
        for row in assets:
            if asset_type_id == row[3]:
                asset_ids.append(row[0])
        return asset_ids

    # This will run when the function is supplied with a symbol and can only return one value
    if symbol != None:
        symbol = symbol.upper()
        assets = get_assets(c)
        for row in assets:
            if symbol in row:
                return row[0]
    

def insert_into_asset_types(cursor, asset_type):
    asset_type = asset_type.capitalize()
    cursor.execute('INSERT INTO asset_types (type) VALUES (?)', (asset_type,))


def insert_into_assets(cursor, symbol, asset_type):
    symbol = symbol.upper()
    asset_type = asset_type.capitalize()
    asset_type_id = get_asset_type_id_for(cursor, asset_type)
    cursor.execute('INSERT INTO assets (symbol, asset_type_id) VALUES (?,?)', (symbol, asset_type_id,))


def insert_into_transactions(cursor, symbol, price, qty, currency='GBP'):
    symbol = symbol.upper()
    currency = currency.upper()
    asset_id = get_asset_id_for(cursor, symbol)
    cursor.execute('INSERT INTO transactions (asset_id, purchase_currency, purchase_price, quantity) VALUES (?,?,?,?)',
            (asset_id, currency, price, qty,)
            )

def update_asset_current_price(cursor, symbol, current_price):
    symbol = symbol.upper()
    asset_id = get_asset_id_for(cursor, symbol)
    cursor.execute('''
    UPDATE assets SET current_price = ? WHERE asset_id = ?
    ''', (current_price, asset_id))




