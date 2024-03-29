from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Instagram:
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        self.bot = webdriver.Firefox()
        
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(10)
        print('ready to go')
        email = bot.find_element_by_name('username')
        pwd = bot.find_element_by_name('password')
        email.clear()
        pwd.clear()

        email.send_keys(self.username)
        pwd.send_keys(self.pwd)
        pwd.send_keys(Keys.RETURN)
        time.sleep(7)

    def find_posts(self, hashtag_name):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag_name + '/')

        time.sleep(5)

        for i in range (1,20):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
        
        time.sleep(5)

        grid_elements = bot.find_elements_by_class_name('v1Nh3')
        links = []
        for element in grid_elements:
            link = element.find_element_by_tag_name('a').get_attribute('href')
            links.append(link)
        print('todos os links:  ', len(links))
        time.sleep(60)
        counter = 0
        for link in links:
            try:
                bot.get(link)

                bot.find_element_by_class_name('dCJp8').click()
                counter +=1
                print(counter, ' likes')
                time.sleep(10)
            except Exception as e:
                time.sleep(60)
                print(e)
            if counter % 30 == 0:
                time.sleep(300)
      

        
        
            

        
        
       
    