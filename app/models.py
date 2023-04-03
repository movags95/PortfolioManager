from config import DB_PATH
import sqlite3

class Asset:
    def __init__(self, symbol, type, path=DB_PATH):
        self.symbol = symbol
        self.type = type
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    # Closes the connection when object is destroyed
    def __del__(self):
        self.conn.commit()
        self.conn.close()
        
    def add_asset_type(self):
        self.cursor.execute("INSERT INTO asset_types (type) VALUES (?)", (self.type,))
        
        

    

if __name__ == '__main__':
    asset = Asset(symbol='AAPL', type='Stock')
    asset.add_asset_type()
    print(asset.symbol)
    print(asset.type)