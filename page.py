import re

#all the common actions are logged in this file.

class Page(object):
    '''
    Base class for all Pages
    '''

        
    def __init__(self, selenium):
        '''
        Constructor of the class
        '''
        self.selenium = selenium
        
        
    def verify_page_title(self, title_regexp):
        '''
        Verify page title
        '''
        if (re.search(title_regexp, self.selenium.get_title()) is None):
            raise Exception,'\r\nPage tile verification failed. Expected: %s; Actual:%s\r\n' %(title_regexp,self.selenium.get_title())
       
        
    def click_link(self, link, wait_flag=False,timeout=80000):
        self.selenium.click("link=%s" %(link))
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
        
    def click(self,locator,wait_flag=False,timeout=80000):
        self.selenium.click(locator)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
            
    def type(self,locator, str):
        self.selenium.type(locator, str)
        
    def click_button(self,button,wait_flag=False,timeout=80000):
        self.selenium.click(button)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)

    def get_url_current_page(self):
        return(self.selenium.get_location())
    
    def is_element_present(self,locator):
        return self.selenium.is_element_present(locator)
    
    def is_text_present(self,text):
        return self.selenium.is_text_present(text)
    
    def refresh(self,timeout=80000):
        self.selenium.refresh()
        #refreshes the page         
        self.selenium.wait_for_page_to_load(timeout)
