# Utility functions for the scraper

import logging

# Custom logging the files
class Log():
    @staticmethod
    def setup_logging():
        logging.basicConfig(filename='scraper/logs/scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def INFO(message):
        logging.info(message)

    @staticmethod
    def ERROR(message):
        logging.error(message)

