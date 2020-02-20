""" Main Code Starts here """

if __name__ == '__main__':
    AC = app.app_context()
    AC.push()
    config_file = "collector.ini"
    if C is None:
        C = Context("Collector Server",config_file)    
    if (C):
        logger = C.logger
        logger.info("****** Collector Server *****************")
        logger.info("%s: as '%s' Using configuration: '%s'"%(sys.argv[0],getpass.getuser(),config_file))
        logger.info("*****************************************")

    manager.run()

