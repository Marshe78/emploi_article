# pip install selenium
# need chrome driver executable in folder
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ouvre la fenetre
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

#
BASE_URL = 'https://jobencomminges.fr/articles'
#BASE_URL = 'https://www.c-chartrespourlemploi.fr/articles'
#BASE_URL = 'https://angers-emploi.fr/articles'
# https://angers-emploi.fr/articles
driver.get(BASE_URL)


data = {}
tab = []
page_num = 1


def find_site():
    global page_num
    x = 0
    time.sleep(1)
    lien_click = driver.find_elements(
        By.CLASS_NAME, 'thumbnail.border-thumbnail.shadow-thumbnail')
    for lien in lien_click:
        time.sleep(2)
        try:
            page_max = driver.find_elements(
                By.CLASS_NAME, 'js-page')
            page_max = page_max[-1].text
            print(page_max)
        except:
            print("page_max, NAN")
        time.sleep(2)
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
            # -- si il a parcouru tous les articles
            if (x == len(new)):
                if(page_num <= page_max):
                    print('change page')
                    change_page(page_num)
                else:
                    print('fin de la boucle')
                    return tab
            tab.append(data)
        except:
            print("Erreur")
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
