""" Module that provides conn object for the model """

import sqlobject

conn = None

def establish_connection(save_type_key):
    """ Connect to the database """
    if save_type_key == "mysql":
        #conn = sqlobject.mysql.builder()()
        pass
    elif save_type_key == "sqll":
        conn = sqlobject.sqlite.builder()("test.db")
        print (conn)
    elif save_type_key == "psql":
        conn = sqlobject == sqlobject.postgres.builder()
