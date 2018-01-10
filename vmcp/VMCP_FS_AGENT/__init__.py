
import time

from op_services import op_cdr as cdr
from op_services import op_config as conf


def main(interval):
	while True:
		_line_number = cdr.get_cdr_last_row_line_number(cdr.get_cdr_last_row_db())
		# print ("##################",_line_number,)
		time.sleep(int(interval))
		# cdr.insert_from_file_to_db(0)

if __name__== "__main__":
	_Service_Data=conf.service_data()
	main(_Service_Data['interval'])