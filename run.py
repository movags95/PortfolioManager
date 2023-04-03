from app.install import create_db, configure_environment, create_requirements_txt, reset_environment, delete_db


if __name__ == '__main__':
    # reset_environment()
    # create_requirements_txt()
    delete_db()
    create_db()
    configure_environment()