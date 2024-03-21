import logging

def setup_logging():
   
    logger = logging.getLogger("custom_logger")
    logger.setLevel(logging.DEBUG)

   
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    
    ch.setFormatter(formatter)

   
    logger.addHandler(ch)

    return logger

if __name__ == "__main__":
    logger = setup_logging()
    logger.debug("Logging setup completed successfully")
