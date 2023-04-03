import os
import sqlite3
from app.config import VIRTUAL_ENV_PATH, REQUIREMENTS_PATH, DB_PATH
from app.helpers import directory_exists, file_exists

# Create the SQLite database
def create_db():
    print('-----------------------------------------------')
    if file_exists(DB_PATH):
        print(DB_PATH + ' exists.')
    else:

        print('Creating ' + DB_PATH)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        # Create tables for stocks, crypto, funds, and cash
        c.execute('''
            CREATE TABLE IF NOT EXISTS asset_types (
                type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS assets (
                asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                current_price REAL,
                FOREIGN KEY(asset_type_id) REFERENCES asset_types(type_id)
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                FOREIGN KEY(asset_id) REFERENCES assets(asset_id),
                purchase_currency TEXT NOT NULL,
                purchase_price REAL NOT NULL,
                quantity REAL NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    print('-----------------------------------------------')

def delete_db():
    print('-----------------------------------------------')
    print('Deleting ' + DB_PATH)
    if file_exists(DB_PATH):
        os.system('rm ' + DB_PATH)
    print('-----------------------------------------------')


# # Install the Flask app
# def create_venv():
#     print('-----------------------------------------------')
#     if directory_exists(VIRTUAL_ENV_PATH) == False:
#         print('Creating Virtual Environment in ' + VIRTUAL_ENV_PATH)
#         print('-----------------------------------------------')
#         os.system('virtualenv ' + VIRTUAL_ENV_PATH)
#         # os.system('chmod +x ' + VIRTUAL_ENV_PATH+'/bin/activate')
#         # os.system('source ' + VIRTUAL_ENV_PATH+'/bin/activate')
#     else:
#         print('Virtual Environment Found: ' + VIRTUAL_ENV_PATH)
#         # os.system('source ' + VIRTUAL_ENV_PATH+'/bin/activate')
#     print('-----------------------------------------------')
#     print('!!!! PLEASE ACTIVATE VENV EG. venv/bin/activate !!!!')
#     print('-----------------------------------------------')

# def install_requirements():
#     print('-----------------------------------------------')
#     if file_exists(REQUIREMENTS_PATH):
#         print('Installing requirements.txt in ' + REQUIREMENTS_PATH)
#         os.system('pip3 install -r ' + REQUIREMENTS_PATH)
#     else:
#         print('Creating requirements.txt file')
#         os.system('pip freeze > ' + REQUIREMENTS_PATH)
#     print('-----------------------------------------------')

# def create_requirements_txt():
#     print('-----------------------------------------------')
#     print('Creating ' + REQUIREMENTS_PATH)
#     os.system('pip freeze > ' + REQUIREMENTS_PATH)
#     print('-----------------------------------------------')

def reset_environment():
    print('-----------------------------------------------')
    print('Clearing environment...')
    os.system('rm ' + REQUIREMENTS_PATH)
    os.system('rm -r ' + VIRTUAL_ENV_PATH)
    os.system('rm ' + DB_PATH)
    print('-----------------------------------------------')




