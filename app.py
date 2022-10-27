# pip install selenium
# need chrome driver executable in folder
from selenium import webdriver
from selenium.webdriver.common.by import By

#Ouvre la fenetre
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

# 
#BASE_URL = 'https://jobencomminges.fr/articles'
BASE_URL = 'https://www.c-chartrespourlemploi.fr/articles'
#BASE_URL = 'https://angers-emploi.fr/articles'
#https://angers-emploi.fr/articles
driver.get(BASE_URL)


import time
data ={}
tab = []
page_num = 1
def find_site():
    global page_num
    x=0
    lien_click = driver.find_elements(By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
    for lien in lien_click:
        new = driver.find_elements(By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
        time.sleep(1)
        new[x].click()
        try:
            attachement_file = driver.find_element(By.CLASS_NAME, 'button-download-attachment-file').text
        except:
            attachement_file = ''
        title = driver.find_element(By.CLASS_NAME, 'frontoffice-title-2019')
        img = driver.find_element(By.CLASS_NAME, 'img-fluid')
        date = driver.find_element(By.CLASS_NAME, 'publication-date-article')
        data['title'] = title.text
        data['attachement_file'] = attachement_file
        data['img'] = img.get_attribute('src')
        data['date'] = date.text
        driver.back()
        time.sleep(2)
        x = x+1
        # -- si il a parcouru tous les articles
        if (x == len(new)): 
            if len(new) > 11:
                change_page(page_num)
                page_num = page_num+1
                find_site()
        tab.append(data)
      
        
    return tab

def change_page(number_clicks):
    for nb in number_clicks:
        btn = driver.find_element(By.CLASS_NAME, 'js-next-page.next-page')
        btn.click()
        time.sleep(1)
    
        
print(find_site())