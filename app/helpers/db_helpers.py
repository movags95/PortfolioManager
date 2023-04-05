def get_asset_types(cursor):
    cursor.execute('SELECT * FROM asset_types')
    return cursor.fetchall()

def get_assets(cursor):
    cursor.execute('SELECT * FROM assets')
    return cursor.fetchall()

def get_transactions(cursor):
    cursor.execute('SELECT * FROM transactions')
    return cursor.fetchall()

def get_currencies(cursor):
    cursor.execute('SELECT * FROM currencies')
    return cursor.fetchall()

def get_asset_type_id_for(cursor, type):
    type = type.capitalize()
    types = get_asset_types(cursor)
    for row in types:
        if type in row:
            return row[0]

def get_asset_id_for(cursor, symbol=None, asset_type_id=None):
    assets = get_assets(cursor)

    # This will run when the function is supplied with an asset_type_id and will return a tuple of values
    if asset_type_id != None:
        asset_ids = []
        for row in assets:
            if asset_type_id == row[4]:
                asset_ids.append(row[0])
        return asset_ids

    # This will run when the function is supplied with a symbol and can only return one value
    if symbol != None:
        symbol = symbol.upper()
        for row in assets:
            if symbol in row:
                return row[0]
            
def get_currency_id_for(cursor, currency_name=None, currency_symbol=None):
    currencies = get_currencies(cursor)

    # Run if currency name is supplied
    if currency_name != None:  
        currency_name = currency_name.upper()
        for row in currencies:
            if currency_name in row:
                return row[0]
    
    # Run if currency symbol is supplied
    if currency_symbol != None:
        for row in currencies:
            if currency_symbol in row:
                return row[0]
        
    
def insert_into_asset_types(cursor, asset_type):
    asset_type = asset_type.capitalize()
    cursor.execute('INSERT INTO asset_types (type) VALUES (?)', (asset_type,))


def insert_into_assets(cursor, symbol, asset_type):
    symbol = symbol.upper()
    asset_type = asset_type.capitalize()
    asset_type_id = get_asset_type_id_for(cursor, asset_type)
    cursor.execute('INSERT INTO assets (symbol, asset_type_id) VALUES (?,?)', (symbol, asset_type_id,))


def insert_into_transactions(cursor, symbol, price, qty, currency_name='GBP'):
    symbol = symbol.upper()
    currency_id = get_currency_id_for(cursor, currency_name=currency_name)
    asset_id = get_asset_id_for(cursor, symbol)
    cursor.execute('INSERT INTO transactions (asset_id, currency_id, purchase_price, quantity) VALUES (?,?,?,?)',
            (asset_id, currency_id, price, qty,)
            )

def update_asset_current_price(cursor, symbol, current_price, currency_name=None, currency_symbol=None):
    symbol = symbol.upper()
    asset_id = get_asset_id_for(cursor, symbol)
    
    if currency_name is not None:
       currency_id = get_currency_id_for(cursor, currency_name=currency_name)
    elif currency_symbol is not None:
        currency_id = get_currency_id_for(cursor, currency_symbol=currency_symbol)
    else:
        raise ValueError('Error: provide at least 1 currency parameter.')
    

    cursor.execute('''
    UPDATE assets SET current_price = ?, currency_id = ? WHERE asset_id = ?
    ''', (current_price, currency_id, asset_id))




