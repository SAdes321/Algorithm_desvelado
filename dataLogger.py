import logging

def logData(message, level = 'info'):

    #Used to log the data to the logfile
    
    if level == 'info':
        logging.info(message)
    elif level == 'critical':
        logging.critical(message)
    elif level == 'warning':
        logging.warning(message) 
    elif level == 'error':
        logging.error(message)
    elif level == 'debug':
        logging.debug(message)
    elif level == 'exception':
        logging.exception(message) 

if __name__ == "__main__":
    pass