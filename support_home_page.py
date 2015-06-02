'''
Created on Jun 21, 2010

@author: mozilla
'''
import sumo_page
import vars

class SupportHomePage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title                   = 'Firefox Support Home Page'
    main_search_box         = 'fsearch-new'
    log_in_link             = 'log in'
    search_button           = 'searchsubmit-new'
    advanced_search_link    = "css=a.home-advanced-search"
    see_all_button          = "button-seeall"
    
    
    def __init__(self,selenium):
        super(SupportHomePage,self).__init__(selenium)
    
    def go_to_support_home_page(self):
        self.selenium.open('/')
        self.verify_page_title(self.title)
                   
    def click_log_in_link(self):
        self.click(self.log_in_link,True,vars.ConnectionParameters.page_load_timeout)
        
    def click_advanced_search_link(self, refine_search_page_obj):
        self.click(self.advanced_search_link,True,vars.ConnectionParameters.page_load_timeout)
        refine_search_page_obj.verify_page_title(refine_search_page_obj.title)
        
    def do_search_on_main_search_box(self, search_query, search_page_obj):
        self.type(SupportHomePage.main_search_box, search_query)
        self.click(self.search_button,True,vars.ConnectionParameters.page_load_timeout)
        search_page_obj.verify_page_title(search_page_obj.title)	