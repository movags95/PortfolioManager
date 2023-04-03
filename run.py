from app.install import create_db, configure_environment, create_requirements_txt, reset_environment


if __name__ == '__main__':
    # reset_environment()
    # create_requirements_txt()
    create_db()
    configure_environment()