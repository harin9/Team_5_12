from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import matplotlib

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

    print(animal, '-', count)
    animal_list.append(animal)
    count_list.append(int(count))
    x.append(cyc)

print('')
print(animal_list)
print(count_list)

max = count_list.index(max(count_list))
print('')
print('속담에 가장 많이 언급된 동물 : ', animal_list[max])

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

plt.bar(x, count_list)
plt.xticks(x, animal_list)
plt.xlabel('동물 이름')
plt.ylabel('속담 개수')
plt.title('동물 이름이 들어간 속담 개수')

plt.show()