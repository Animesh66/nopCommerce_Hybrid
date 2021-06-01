import logging


# this file will generate INFO log for test cases
class LogGeneration:
    @staticmethod
    def log_generation():
        logging.basicConfig(filename='/Users/animeshmukherjee/Desktop/Animesh/Log_file/nopcommerce_login.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
