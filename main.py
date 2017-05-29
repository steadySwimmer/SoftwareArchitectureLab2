from configuration.configParser import *

from Connection import *

if __name__ == '__main__':
	result_dict = config_parser_result()

	establish_connection(result_dict[save_type_key])