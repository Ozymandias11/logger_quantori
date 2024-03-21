import logging
import logging.config
from CustomHandler import CustomHandler

def apply_logging_configuration():
    
    logging.config.fileConfig('logging.conf')

   
    logger = logging.getLogger("custom_logger")

    # Log messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # Close database connection
    for handler in logger.handlers:
        if isinstance(handler, CustomHandler):
            handler.close()

if __name__ == "__main__":
    apply_logging_configuration()
