
import time

from op_services import op_cdr as cdr 
from op_services import op_config as config


def main(interval):
	while True:
		cdr.()
		time.sleep(int(interval))
  
if __name__== "__main__":
	_Service_Data=conf.service_data()
	main(_Service_Data['interval'])