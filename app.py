# pip install selenium
# need chrome driver executable in folder
# pip install mysql.connector
import time
from types import new_class
from selenium import webdriver
from selenium.webdriver.common.by import By
from pipelines import Database

# Ouvre la fenetre
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

BASE_URL = 'https://jobencomminges.fr/articles'
#BASE_URL = 'https://www.c-chartrespourlemploi.fr/articles'
#BASE_URL = 'https://angers-emploi.fr/articles'
# https://angers-emploi.fr/articles
driver.get(BASE_URL)


data = {}
tab = []
page_num = 1
x = 0

def find_site():
    Database.connectDb()
    Database.createTable()
    global page_num
    global x
    time.sleep(1)
    lien_click = driver.find_elements(
        By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
    for lien in lien_click:
        try:
            page_max = driver.find_elements(
                By.CLASS_NAME, 'js-page')
            page_max = page_max[-1].text
        except:
            print("page_max, NAN")
        try:
            new = driver.find_elements(
                By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
            new[x].click()
            try:
                attachement_file = driver.find_element(
                    By.CLASS_NAME, 'button-download-attachment-file').text
                data['attachement_file'] = attachement_file
            except:
                attachement_file = ''
            try:
                title = driver.find_element(
                    By.CLASS_NAME, 'frontoffice-title-2019')
                data['title'] = title.text
            except:
                data['title'] = None
            try:
                img = driver.find_element(By.CLASS_NAME, 'img-fluid')
                data['img'] = img.get_attribute('src')
            except:
                data['img'] = None
            try:
                date = driver.find_element(
                    By.CLASS_NAME, 'publication-date-article')
                data['date'] = date.text
            except:
                data['date'] = None

            driver.back()
            time.sleep(2)
            x = x+1
            print(x)
            print(len(new))
            print('-----')
            # -- si il a parcouru tous les articles
            if (x == len(new)):
                # 2 correspond au nombre de pages
                if(page_num < 2 ):
                    print('change page')
                    x = 0
                    change_page(page_num)
                else:
                    print('fin de la boucle')
                    return tab
            # il a passer la 1ere page et est revenu à la page 1 (il doit retourner à sa page)
            elif page_num > 1:
                change_page(page_num)

            tab.append(data)
            Database.addRowEmploi(data)
        except:
            print("fin du script")
    return tab


def change_page(number_clicks=0):
    global page_num
    for i in range(0, number_clicks):
        btn = driver.find_element(By.CLASS_NAME, 'js-next-page.next-page')
        btn.click()
        time.sleep(1)
        page_num = page_num + 1
        find_site()


print(find_site())

driver.quit()
