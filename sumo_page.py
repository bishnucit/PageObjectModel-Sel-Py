from page import Page
import vars

import sys
import time
import re

page_load_timeout = vars.ConnectionParameters.page_load_timeout

class SumoPage(Page):
    
    def __init__(self,selenium):
        super(SumoPage,self).__init__(selenium)
        
    log_out_link       =  "css=a[href *='logout']"
    my_account_link    = "css=a[href *='user_preferences']"
    contribute_link    = "css=a[href *= 'contribute']"
    kb_link            = "css=a[href = '/kb/']"
    support_forum_link = "css=a[href = '/forum']"
    question_link      = "css=a[href *= 'question']"
    other_link         = "css=a[href *= 'Other']"
    login_link         = "css=a[href *= 'login']"
    
    def log_out(self):
        self.click(self.log_out_link, True)
        
    def open(self,url,count=0):
        try:
            self.selenium.open(url)
            is_page_500   = re.search("500", self.selenium.get_title())
            is_page_error = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
            is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
            if ((is_page_500 is not None or is_page_error is not None or is_page_problem is not None ) and count < 10):
                    count=count+1
                    self.open(url, count)
        except Exception, e:
            if count < 10:
                count = count+1
                self.open(url, count)
                time.sleep(2)
            else:
                if self.is_text_present("Search Unavailable"):
                    print "Search unavailable"
                print e
                print "\n--------------------------\n"
                print self.selenium.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)
                
    def click(self,locator,wait_flag=False,timeout=80000):
        count=0
        try:
            self.selenium.click(locator)
            if(wait_flag):
                self.selenium.wait_for_page_to_load(timeout)
                is_page_500     = re.search("500", self.selenium.get_title())
                is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None ) and count < 10):
                        count=count+1
                        self.refresh(timeout)
                        is_page_500     = re.search("500", self.selenium.get_title())
                        is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
        except Exception, e:
            if( wait_flag and count < 10):
                is_page_500     = re.search("500", self.selenium.get_title())
                is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None ) and count < 10):
                        count=count+1
                        self.refresh(timeout)
                        is_page_500     = re.search("500", self.selenium.get_title())
                        is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
            else:
                print self.selenium.get_title()
                print e
                print "\n--------------------------\n"
                print self.selenium.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)