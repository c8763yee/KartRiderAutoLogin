from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from accpw import fetchFrom #require accpw.py and json that contain account and password


class Beanfun():
    def __init__(self):
        self.web = webdriver.Firefox()
        self.web.get('https://tw.beanfun.com/')
        self.find = self.web.find_element

    def login(self):
        self.find(By.ID, 'BF_anchorLoginBtn').click()
        self.web.switch_to.frame(self.find(By.ID, 'ifmForm1'))
        acc, pw = fetchFrom('Beanfun')
        self.find(By.NAME, 't_AccountID').send_keys(acc)
        self.find(By.NAME, 't_Password').send_keys(pw)
        self.find(By.ID, 'btn_login').click()

    def login_game(self):
        self.web.get('https://tw.beanfun.com/game_zone/')
        self.find(By.CLASS_NAME, 'BF_Content').find_element(By.TAG_NAME, 'li').click()
        self.web.switch_to.frame(self.find(By.NAME, 'fbContent'))

        try:
            never_remind = self.webDriverWait(self.web, 10).until(
                EC.element_to_be_clickable(self.find(By.ID,'cbxRemoveServiceFriendlyReminder')))
            if not never_remind.is_selected():
                never_remind.click()
            
        except NoSuchElementException:
            pass

        self.find(By.ID,'btnFriendlyReminderOK').click()
        
    def start(self):
        self.login()
        self.login_game()
        
Beanfun().start()