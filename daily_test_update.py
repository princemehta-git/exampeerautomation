import pandas as pd
from datetime import datetime
import os
import calendar
import shutil



bio_firstID =  12095  #NEED TO CHANGE
total_file_2create = 31 #NEED TO CHANGE
start_date = 1 #NEED TO CHANGE





bank_firstID = bio_firstID + 124
shutil.rmtree('ready_excels', ignore_errors=True)
os.mkdir('ready_excels')
subs = ['bank', 'eng', 'quant', 'reason', 'gk']
subjects = ['biology', 'chemistry', 'mathematics', 'physics']
currentMonth = datetime.now().month
currentYear = datetime.now().year


for i in range(total_file_2create):
    for count, sub in enumerate(subs):
        df = pd.read_excel('excels\\'+sub+'.xlsx')

        df = df.loc[(i*10):((i*10)+9)]

        df = pd.DataFrame({None:['']}).append(df, ignore_index=True)


        df.iloc[1:, 11] = bank_firstID+(31*count) + i   # NEED TO CHANGE



        df.drop(df.columns[[0]], axis = 1, inplace=True)


        df.to_excel('ready_excels\\'+sub+" "+str(start_date+i)+" "+ calendar.month_abbr[currentMonth]+" "+ str(currentYear)+'.xls',  header = None, index=False)

        print('created: '+sub+" "+str(start_date+i)+" "+ calendar.month_abbr[currentMonth]+" "+ str(currentYear)+'.xls')

    for count1, subject in enumerate(subjects):
        try:
            with open('excels\\' + subject + '\\' + str(start_date+i) + '\\' +'used.txt') as file:
                to_use = int(file.readline())
        except:
            with open('excels\\' + subject + '\\' + str(start_date+i) +'\\' + 'used.txt','w') as file:
                file.write('1')
                to_use = 0
        with open('excels\\' + subject + '\\' + str(start_date+i) +'\\' +'used.txt','w') as file:
            to_write = (to_use+1)%5
            if to_write == 0:
                to_write = 5

            file.write(str(to_write))



        df = pd.read_excel('excels\\' + subject + '\\' + str(start_date+i) + '\\' + str(to_write)+'.xlsx')

        df = df.loc[0 : 9]

        df = pd.DataFrame({None: ['']}).append(df, ignore_index=True)

        df.iloc[1:, 11] = bio_firstID + (31 * count1) + i  # NEED TO CHANGE

        df.drop(df.columns[[0]], axis=1, inplace=True)

        df.to_excel('ready_excels\\' + subject + " " + str(start_date + i) + " " + calendar.month_abbr[currentMonth] + " " + str(
                currentYear) + '.xls', header=None, index=False)
        print('created:  '+ subject + " " + str(start_date + i) + " " + calendar.month_abbr[currentMonth] + " " + str(
                currentYear) + '.xls')


print("\n\nALL FILE CREATED SUCCESSFULLY :)\n\n ")


'''now manual saves'''

import pyautogui
from time import sleep
import os
import subprocess

# input('Enter when you are ready for ctrl save!!!')
# sleep(3)


total_file = os.listdir('ready_excels')


for file in total_file:
    subprocess.call('explorer ready_excels\\'+str(file), shell=True)
    sleep(2)
    with pyautogui.hold('ctrl'):
        pyautogui.press('s')

    sleep(0.5)
    with pyautogui.hold('alt'):
        pyautogui.press('f4')
    sleep(0.5)

print('\n\nSUCCESSFULLY SAVED ALL FILES\n\n')




'''Uploading and Importing all files'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
# from time import sleep
from concurrent.futures import ThreadPoolExecutor

import os

no_of_threads = 5

uploaded_list = []


def upload_import(thread_num):
    options = webdriver.ChromeOptions()
    options.headless = True
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    # options.add_argument("--app=https://www.google.com")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])


    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    driver.get('http://center3.exampeer.in/center/index.php')
    driver.find_elements_by_xpath("//input[@name = 'email']")[0].send_keys('exampeer1@gmail.com')
    driver.find_elements_by_xpath("//input[@name = 'password']")[0].send_keys(123456)
    driver.find_elements_by_xpath("//input[@value = 'login']")[0].click()

    # FILE DIRECTORY
    files = os.listdir('ready_excels')
    file_path = 'C:\\Users\\PRINCE MEHTA\\PycharmProjects\\Rough_automation\\ready_excels'
    total_files = len(files)



    driver.get('http://center3.exampeer.in/center/import_table.php')
    for count, file in enumerate(files):
        if file not in uploaded_list:
            uploaded_list.append(file)
            while True:
                try:
                    driver.find_elements_by_xpath("//input[@type='text']")
                    break
                except:
                    driver.get('http://center3.exampeer.in/center/import_table.php')

            driver.find_elements_by_xpath("//a[@href = '#add']")[0].click()

            driver.find_elements_by_xpath("//input[@type = 'file']")[0].send_keys(file_path+'\\'+file)
            driver.find_elements_by_xpath("//button[@type = 'submit']")[0].click()
            # sleep(3)
            print('uploaded: ', file, count+1, '/', total_files)
            try:
                name = quote(file)
            except:
                name = str(file)

            driver.get('http://center3.exampeer.in/center/import.php?import=' + name)
            print('imported: ', file, count+1, '/', total_files)
    driver.quit()


with ThreadPoolExecutor(max_workers=25) as executor:
    executor.map(upload_import, list(range(no_of_threads)))

print('ALL UPLOADED AND IMPORTED :)')