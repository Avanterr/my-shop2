import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img")
ruby.click()
time .sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
review =  driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a")
review .click()
time .sleep(3)
star5 = driver.find_element_by_css_selector("#commentform > p.comment-form-rating > p > span > a.star-5")
star5 .click()
driver.execute_script("window.scrollBy(0, 900);")
comment = driver.find_element_by_name("comment")
comment.send_keys("Nice book!")
time .sleep(3)
name = driver.find_element_by_name("author")
name.send_keys("Rasul")
time .sleep(3)
email = driver.find_element_by_name("email")
email.send_keys("Rasul@mail.ru")
time .sleep(3)
submit = driver.find_element_by_id("submit")
submit . click()
