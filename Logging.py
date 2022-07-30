import logging
logging.basicConfig(filename="logging",level=logging.INFO)
logging.info("This is my very first code for loggging")
l=[1,3,2,4,5,6,7,7]
for i in l:
    if i == 2:
        logging.info(i)
logging.warning("this will tryy to load warning messages")
logging.error("this is a error message froom the system")
logging.shutdown()