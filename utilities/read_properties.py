# this file will read the data present in config.ini file
import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    @staticmethod  # this is a static method means it can be called directly from class without creating object
    def get_application_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('common data', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password
