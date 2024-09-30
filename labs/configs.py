"""module for parsing config for environment from arguments"""
import os
import configparser


def parse_config():
    """function for reading config.ini and for dic creation"""
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__) + '/config.ini')
    return config
