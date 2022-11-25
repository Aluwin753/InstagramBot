from Auth import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random

browser = None
def login_firefox(login, password):
    global browser
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get("https://www.instagram.com")
    time.sleep(random.randrange(2, 5))

    _login = browser.find_element(By.NAME, 'username')
    _login.clear()
    _login.send_keys(login)

    time.sleep(random.randrange(1, 6))

    _password = browser.find_element(By.NAME, 'password')
    _password.clear()
    _password.send_keys(password)

    time.sleep(random.randrange(2, 8))

    _password.send_keys(Keys.ENTER)

    time.sleep(random.randrange(3,6))

    #_login_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    #_login_button.click() - это альтернатива кнопки Enter

def close_browser():
    global browser
    browser.close()
    browser.quit()

def search_by_hashtag(hashtag):
    global browser
    browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")

    for i in range(1,4):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(2, 5))

    hrefs = browser.find_elements(By.TAG_NAME, 'a')
    urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
    print(urls)


    for url in urls:
        browser.get(url)
        time.sleep(random.randrange(80, 120))
        like = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
        like.click()
        time.sleep(random.randrange(80, 105))

login_firefox(login, password)
time.sleep(2)
search_by_hashtag("прикол")
time.sleep(5)
close_browser()