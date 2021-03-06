import logging


class Logger:
    def __init__(self,logger_name = None):
        if logger_name:
            self.logger = logging.getLogger(logger_name)
        else:
            self.logger = logging.getLogger()
        self.set_debug_level()

    def set_path(self,path):
        self.file_handler = logging.FileHandler(path)
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler) 
        
       

    def set_debug_level(self):
        self.logger.setLevel(logging.DEBUG) 

     
    
    def info(self,msg):
        self.logger.info(msg)

    def error(self,msg):
        self.logger.error(msg)






if __name__ == "__main__":
    logger = Logger()
    logger.set_path('/home/nmgfrank/log.txt')
    logger.set_debug_level()
    logger.info("test")

