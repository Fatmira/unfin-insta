import requests
import pdb
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#unfinished

print("")
print("Instagram")
print("Made by Hunter")
print("")

def login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.instagram.com/accounts/login/")
    dom = driver.find_element_by_xpath("//*")

    pdb.set_trace()
    username = dom.find_element_by_name("username")
    password = dom.find_element_by_name("password")
    login_button = dom.find_element_by_xpath('//*[@class="_qv64e _gexxb _4tgw8 _njrw0"]')

    username.clear()
    password.clear()
    username.send_keys("Username: ")
    password.send_keys("Password: ")

    login_button.click()
    driver.get("https://www.instagram.com/accounts/login")

login()

def main():
    target = input("Target Username:  ")
    sleep(1)
    print("")
    print("Link: https://www.instagram.com/" + str(target + "/?__a=1"))
    print("")
    sleep(2)
    site = ("https://www.instagram.com/ " + target + "/__a=1")

    headers = {
        "Useragent": 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1ua.safari'}

    t_insta = requests.get(site, headers=headers)
    soup = BeautifulSoup(t_insta.content, 'html.parser')

    match = soup.find("_class_")
    print(match)

main()
