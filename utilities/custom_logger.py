import logging


# this file will generate INFO lo for test cases
class LogGeneration:
    @staticmethod
    def log_generation():
        logging.basicConfig(filename="/logs/automations.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
