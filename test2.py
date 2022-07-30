import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    logging.info("i'm trying to read a file")
    with open("test.txt", "r"):
        logging.info("it has successfully read the file")
except  Exception as e:
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)
