import os

def directory_exists(path):
    return os.path.isdir(path)

def file_exists(path):
    return os.path.isfile(path)