# pip install selenium
# need chrome driver executable in folder
from selenium import webdriver
from selenium.webdriver.common.by import By
from pipelines import Database

#Ouvre la fenetre
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

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
    Database.connectDb()
    Database.createTable()
    global page_num
    x=0
    time.sleep(1)
    lien_click = driver.find_elements(By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
    for lien in lien_click:
        new = driver.find_elements(By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
        #print(new[0])
        time.sleep(1)
        try:
            new[x].click()
            time.sleep(1)
        except:
            print('ERROOOORRRR')
            
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
            change_page(page_num)
        tab.append(data)
        Database.addRow(data)
       
    return tab

def change_page(number_clicks = 0):
    global page_num
    for i in range(0, number_clicks):
        btn = driver.find_element(By.CLASS_NAME, 'js-next-page.next-page')
        btn.click()
        time.sleep(1)
        page_num = page_num +1
        find_site()
    
        
print(find_site())