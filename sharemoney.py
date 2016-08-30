import numpy as np
import sqlite3
import glob

_reference_cursor = [None]

def get_shared_money(*args):
    main_command = args[0]
    parameters = args[1]
    if main_command == "create":
        result = create_db(parameters)
    elif main_command == "list":
        result = list_db()
    return result
    # print "args",args
    # reference_cursor[0] = int(args[0]) # to be implemented

def create_db(name):
    files = glob.glob("./db_folder/{}.db".format(name))
    if files:
        return "DataBase exists, please change the name"
    else:
        conn = sqlite3.connect('./db_folder/{}.db'.format(name))
        c = conn.cursor()
        _reference_cursor[0] = c
        return "DataBase {} Created".format(name)

def list_db(*args): # to do debugging
    files = glob.glob("./db_folder/*.db")
    file_names = [i[12:-3] for i in files]
    result = "\n".join(file_names)
    return result
