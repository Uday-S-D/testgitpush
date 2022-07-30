import logging
logging.basicConfig(filename="Test.log",level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')
logging.info("This is my time stamp")