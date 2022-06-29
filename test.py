import logging
logging.basicConfig(filename="test1.log",level = logging.INFO)
logging.info("this in my very first code for logging")
logging.warning("this will try to load warning message")
logging.error("this ia an error msg from system")
l = [1,2,3,4,5,667,7]
for i in l:
    if i ==2 :
        logging.info(l)
        logging.warning("this is a warning for user that they have found 2 in list")
logging.shutdown()