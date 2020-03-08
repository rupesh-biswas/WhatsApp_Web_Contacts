from time import sleep
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytictoc import TicToc
t = TicToc()
t.tic()

options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

delay = 30 # seconds
chat_icon = WebDriverWait(driver, delay).until(EC.presence_of_element_located((
    By.XPATH, '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span')))
chat_icon.click()

scroll_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((
    By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]')))
sleep(3)

people=[]
ht = driver.execute_script("return arguments[0].scrollHeight;", scroll_box)
last_ht=0
while last_ht <= ht:
    sleep(1)
    persons = driver.find_elements_by_class_name('_3NWy8')
    for person in persons:
        temp_people=person.text
        if temp_people != '' and temp_people not in people:
            people.append(temp_people)
    last_ht = driver.execute_script(f"""arguments[0].scrollTo({last_ht}, {last_ht+72*15}); 
                                    return {last_ht+72*15}""",scroll_box)
    df=pd.DataFrame(people)
    df.to_csv('peoples.csv',index=False)
    print(df.shape[0])
driver.quit()
print(t.toc())
