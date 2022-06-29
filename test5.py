import logging

logging.basicConfig(filename="test5.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s)')

try:
    logging.info("I am trying to read a file")
    with open('sudh.txt','r'):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this is critical")
    logging.error(e)
    logging.exception(e)