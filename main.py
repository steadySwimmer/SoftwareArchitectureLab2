from configuration.configParser import *

import Connection as cn

from Model import Model

if __name__ == '__main__':
	result_dict = config_parser_result()

	model = Model()


	# model.create_user('Batya', 30)
	# model.create_user('Vanyok', 20)
	# model.create_user('Vlados', 19)

	# model.add_book('Romeo', 'pol')
	# model.add_book('Julie', 'rene')
	# model.add_book('Maria', 'lema')

	# model.take_book('Batya', 'Maria')
	model.return_book('Batya', 'Maria')

	print (model.user_list)
	print (model.book_list)
