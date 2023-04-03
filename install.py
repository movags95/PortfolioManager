from app.initialise import delete_db, create_db
import sys


if __name__ == '__main__':
    delete_db()
    create_db()
    