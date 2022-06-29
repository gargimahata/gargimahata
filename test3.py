import logging

logging.basicConfig(filename="test6.log", level=logging.WARNING, format='%(levelname)s %(asctime)s %(name)s %(message)s)')


def devide(a, b):
    logging.info("number entered by used is %s and %s", a, b)
    try:
        logging.info("we are into function.")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info("result = %s", div)
        return div
    except Exception as e:
        logging.exception(e)
        print(e)



print((devide(3, 0)))
