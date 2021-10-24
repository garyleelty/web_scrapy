import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import time


browser = webdriver.Chrome('/Users/gary/c/chromedriver')
browser.get('http://iecms.mofcom.gov.cn')
p = input('验证码')

name = []

file = open('name.csv')
csvreader = csv.reader(file)
for line in csvreader:
    name.append(line)
#print(name)
c = len(name)
print(c)
textfile = open("a_file.txt", "w")
for d in range(c):
    url = 'https://iecms.mofcom.gov.cn/pages/corp/NewCMvCorpInfoTabList.html?sp=S&sp=S{}&sp=S&sp=Ssearch&sp={}'.format(name[d][0],p)
    browser.get(url)
    try:
        item = browser.find_element_by_xpath("//td[@class='f-tac']/a").get_attribute('href')
        browser.get(item)

        doc =browser.page_source

        soup = BeautifulSoup(doc, 'html.parser')

        all_font_tags = soup.find_all('td')
        
        for x in all_font_tags:
            textfile.write(x.text.strip()+ "\t")
        textfile.write("\n")
        time.sleep(15)
    except:
        print(name[d][0])
        time.sleep(15)
textfile.close()




'<input type="text" name="corpNaCn" value="" id="corpNaCn" class="u-ipt">'
