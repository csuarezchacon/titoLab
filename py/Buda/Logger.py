import logging
import os.path

def initialize_logger(output_dir):
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	
	# create console handler and set level to info
	handler = logging.StreamHandler()
	handler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	
	# create warning file handler and set level to warning
	handler = logging.FileHandler(os.path.join(output_dir, "warning.log"),"w", encoding=None, delay="false")
	handler.setLevel(logging.WARNING)
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	
	# create error file handler and set level to error
	handler = logging.FileHandler(os.path.join(output_dir, "error.log"),"w", encoding=None, delay="true")
	handler.setLevel(logging.ERROR)
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	
	# create debug file handler and set level to debug
	handler = logging.FileHandler(os.path.join(output_dir, "all.log"),"w")
	handler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
	handler.setFormatter(formatter)
	logger.addHandler(handler)