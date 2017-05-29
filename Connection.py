""" Module that provides conn object for the model """

import os
import sqlobject
from configuration.configParser import *

def establish_connection():
    """ Connect to the database """
    res_dict = config_parser_result()
    db_filename = os.path.abspath("mdata.db")

    if res_dict[save_type_key] == "mysql":
        connection_str = "mysql://host" + db_filename
        conn = sqlobject.connectionForURI(connection_str)
    elif res_dict[save_type_key] == "sqll":
        connection_str = "sqlite:" + db_filename
        conn = sqlobject.connectionForURI(connection_str)
    elif res_dict[save_type_key] == "psql":
        connection_str = "postgres://host" + db_filename
        conn = sqlobject.connectionForURI(connection_str)

    #sqlobject.sqlhub.processConnection = conn
    return conn