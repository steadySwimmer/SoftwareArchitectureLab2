""" Module that provides conn object for the model """

import os
import sqlobject

conn = None

def establish_connection(save_type_key):
    """ Connect to the database """
    db_filename = os.path.abspath("mdata.db")
    if save_type_key == "mysql":
        connection_str = "mysql://host" + db_filename
        conn = sqlobject.connectionForURI(connection_str)

    elif save_type_key == "sqll":
        connection_str = "sqlite:" + db_filename
        conn = sqlobject.connectionForURI(connection_str)

    elif save_type_key == "psql":
        connection_str = "postgres://host" + db_filename
        conn = sqlobject.connectionForURI(connection_str)
