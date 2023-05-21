import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To stay within the browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Path of the webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

#Pick the browser you want to use
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.amazon.com")
print(driver.title)

#Serach box element by ID
search = driver.find_element("id", "twotabsearchtextbox")
search.send_keys("Iphone")
search.send_keys(Keys.RETURN)



# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "B09G952BYG"))
#     )
#     print(element)
# finally:
#     driver.quit()

# #Getting the prices of first 5 searches
# search1 = driver.find_element("tag", "a-size-mini a-spacing-none a-color-base s-line-clamp-2")
# print(search1)
# # print(search1)
# # for i in search1:
# #     print(i)


signin = driver.find_element(By.LINK_TEXT,"Apple")
print(signin.tag_name)

# for i in signin:
#     phn = i.find_element(By.CSS_SELECTOR,".data_asin")
#     print(phn.text)
# print(signin.text)


