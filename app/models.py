from config import DB_PATH
import sqlite3
import helpers.db_helpers as db_helpers

class Asset:
    def __init__(self, symbol, type, path=DB_PATH):
        # Set up variables
        self.symbol = symbol.upper()
        self.type = type.capitalize()
        # Connect to DB
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    # Closes the connection when object is destroyed
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    '''
    Asset_types functions
    '''
    # Checks if asset type exists in asset_types table
    def asset_type_exists(self):
        self.cursor.execute("SELECT count(*) FROM asset_types WHERE type = ?", (self.type,))
        return self.cursor.fetchone()[0] > 0

    # Inserts a new asset type into asset_types table
    def add_asset_type(self):
        # Check if asset type exists
        if not self.asset_type_exists():
            self.cursor.execute("INSERT INTO asset_types (type) VALUES (?)", (self.type,))
        else: 
            print(f'Info: Asset type, {self.type} already exists.')
    
    # Get asset_type_id
    def get_asset_type_id(self):
        if self.asset_type_exists():
            self.cursor.execute("SELECT type_id FROM asset_types WHERE type = ?", (self.type,))
            return self.cursor.fetchone()[0]
        else:
            print(f'Info: Unable to get type_id. Type {self.type} does not exist')

    '''
    Assets functions
    '''
    # Checks if asset exists in assets table
    def asset_exists(self):
        self.cursor.execute("SELECT count(*) FROM assets WHERE symbol = ?", (self.symbol,))
        return self.cursor.fetchone()[0] > 0

    # Inserts a new asset into assets table
    def add_asset(self):
        # Find asset_type_id
        self.type_id = self.get_asset_type_id()
        # Check if asset exists
        if not self.asset_exists():
            self.cursor.execute("INSERT INTO assets (symbol, asset_type_id) VALUES (?, ?)", (self.symbol, self.type_id,))
        else: 
            print(f'Info: Asset, {self.symbol} already exists.')
    
    # Get asset_id
    def get_asset_id(self):
        if self.asset_exists():
            self.cursor.execute("SELECT asset_id FROM assets WHERE symbol = ?", (self.symbol,))
            return self.cursor.fetchone()[0]
        else:
            print(f'Info: Unable to get asset_id for asset, {self.symbol} does not exist')
        


if __name__ == '__main__':
    # asset = Asset(symbol='xyz', type='stock')
    # # asset = Asset()
    # asset.add_asset_type()
    # asset.add_asset()
    # print(asset.type)
    # print(asset.symbol)
    # print(asset.type_id)
    # print(asset.get_asset_id())
    conn = sqlite3.connect(DB_PATH)
    types = db_helpers.get_asset_types()
    asset_type_id = db_helpers.get_asset_type_id_for('crypto')
    # db_helpers.insert_into_assets('msft', 'stock')
    print(types)
    print(asset_type_id)
    print(db_helpers.get_assets())

    
    
    
