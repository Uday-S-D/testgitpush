import logging
logging.basicConfig(filename="test1.log",level=logging.INFO,format='%(asctime)s %(name)s %(levelname)s %(message)s')

def divide(a,b):
    logging.info("THE NUMBER ENTERED BY USER IS %s and %s", a,b)
    try:
        logging.info("We are into function")
        div=a/b
        logging.info("we have completed division expression")
        return div
    except Exception as e:
        logging.exception(e)


(divide(3,0))
