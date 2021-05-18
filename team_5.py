from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = 'https://ko.dict.naver.com/#/main'

options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(URL)
driver.implicitly_wait(time_to_wait=30)

ani=input('동물이름 : ').split(',')

animal_list = []
count_list = []
x = []
cyc = 0
for animal in ani:
    cyc += 1
    driver.find_element_by_id('ac_input').send_keys(animal)
    driver.find_element_by_class_name('btn_search').send_keys(Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div/div/a[3]').click()

    count = driver.find_element_by_xpath('//*[@id="searchPage_idioms"]/div[1]/div/span[2]/a/label/span[2]').text

    driver.find_element_by_id('ac_input').clear()