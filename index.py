import time
from selenium import webdriver
from logger import Logger

PATH = "C:\Program Files (x86)\chromedriver.exe"

mylogger = Logger(logger = 'TestMyLog' ).getlog()


class  TestMyLog (object) :

    def  print_log (self) :
        
        driver = webdriver.Chrome(PATH)
        mylogger.info( "Open the browser" )
        driver.maximize_window()
        mylogger.info( "Maximize the browser window." )
        driver.implicitly_wait( 8 )
        driver.get( "https://www.linkedin.com/in/amans199" )
        mylogger.info( "Open Amans199's linkedin account." )
        time.sleep( 1 )
        mylogger.info( "Pause for one second." )
        
        try:
            driver.find_element_by_id( "login-email" ).send_keys( " " )
            mylogger.info( "Enter the email address." )
            driver.find_element_by_id( "login-password" ).send_keys( " " )
            mylogger.info( "Enter the password." )
            driver.find_element_by_id( "login-submit" ).click()
            mylogger.info( "Click the login button." )
            time.sleep( 1 )
            mylogger.info( "Pause for one second." )
        except  Exception as e :
            mylogger.error( "Error found: " + str( e ) )
            # GO TO TRELLO AND PUBLISH A NEW TASK IN THE ERRORS FROM SELENIUM COLUMN    
            
        driver.quit()
        mylogger.info( "Close and exit the browser." )

testlog = TestMyLog()
testlog.print_log()