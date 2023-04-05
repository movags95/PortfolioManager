from app.helpers.db_helpers import *
import sqlite3
from app.config import DB_PATH
from app.initialise import delete_db, create_db
import os


def test_get_asset_types():
    # Create a test database with sample data
    delete_db()
    create_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO asset_types (type) VALUES ('Stock')''')
    c.execute('''INSERT INTO asset_types (type) VALUES ('Bond')''')
    conn.commit()

    # Test that the function returns all asset types
    expected_output = [(1, 'Stock'), (2, 'Bond')]
    actual_output = get_asset_types(c)
    assert actual_output == expected_output

    # # Test that the function returns an empty list when there are no asset types
    # c.execute('''DELETE FROM asset_types''')
    # conn.commit()
    # expected_output = []
    # actual_output = get_asset_types(c)
    # assert actual_output == expected_output
    conn.close()


def test_get_assets():
    # delete_db()
    # create_db()
    # Create a test database with sample data
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO assets (symbol, asset_type_id) VALUES ('AAPL', 1)''')
    c.execute('''INSERT INTO assets (symbol, asset_type_id) VALUES ('GOOG', 1)''')
    c.execute('''INSERT INTO assets (symbol, asset_type_id) VALUES ('IBM', 1)''')
    c.execute('''INSERT INTO assets (symbol, asset_type_id) VALUES ('TSLA', 1)''')
    conn.commit()

    # Test that the function returns all assets
    expected_output = [(1, 'AAPL', None, None, 1), (2, 'GOOG', None, None, 1), (3, 'IBM', None, None, 1), (4, 'TSLA', None, None, 1)]
    actual_output = get_assets(c)
    assert actual_output == expected_output

    # Clean up the test database
    conn.close()

def test_get_transactions():
    # Create a test database with sample data
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO transactions (asset_id, currency_id, purchase_price, quantity) VALUES (1, 2, 100.00, 10)''')
    c.execute('''INSERT INTO transactions (asset_id, currency_id, purchase_price, quantity) VALUES (1, 1, 110.00, 5)''')
    conn.commit()

    # Test that the function returns all
    expected_output = [(1, 1, 2, 100.0, 10), (2, 1, 1, 110.00, 5)]
    actual_output = get_transactions(c)
    assert actual_output == expected_output

    conn.close()

def test_get_currencies():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    actual_result = get_currencies(c)
    actual_result = [(1, 'GBP', '£'), (2, 'USD', '$'), (3, 'EUR', '€')]

def test_get_asset_type_id_for():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Test that the function can handle lowercase inputs
    type = 'stock'
    actual_output = get_asset_type_id_for(c, type)
    expected_output = 1
    assert actual_output == expected_output
    # Test that the function can handle uppercase inputs
    type = 'BOND' 
    actual_output = get_asset_type_id_for(c, type)
    expected_output = 2
    assert actual_output == expected_output

    conn.close()

def test_get_asset_id_for():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Test that that symbol input works
    actual_output = get_asset_id_for(c, symbol='ibm')
    expected_output = 3
    assert actual_output == expected_output

    # Test that asset type id input works 
    actual_output = get_asset_id_for(c, asset_type_id=1)
    expected_output = [1, 2, 3, 4]
    assert actual_output == expected_output

    conn.close()
    
def test_insert_into_asset_types():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    insert_into_asset_types(c, 'Crypto')
    conn.commit()

    actual_output = get_asset_type_id_for(c, 'Crypto')
    expected_output = 3
    assert actual_output == expected_output

    conn.close()

def test_insert_into_assets():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    insert_into_assets(c, 'ada', 'crypto')
    conn.commit()

    expected_result = (5, 'ADA', None, None, 3)
    actual_result = get_assets(c)[-1]
    assert actual_result == expected_result

    conn.close()

def test_insert_into_transactions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    insert_into_transactions(c, 'ada', 103.5, 3400)
    conn.commit()

    actual_result = get_transactions(c)[-1]
    expected_result = (3, 5, 1, 103.5, 3400)
    assert actual_result == expected_result

    conn.close()

def test_update_asset_current_price():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    update_asset_current_price(c, 'ada', 0.4, currency_symbol='$')
    conn.commit()

    actual_result = get_assets(c)[-1]
    expected_result = (5, 'ADA', 0.4, 2, 3)
    assert actual_result == expected_result

    conn.close()

