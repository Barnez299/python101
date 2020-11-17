import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an infor message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# https://www.youtube.com/watch?v=p0A4CV4MWd0&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=10

# json format logger - https://pypi.org/project/python-json-logger/
# https://github.com/madzak/python-json-logger