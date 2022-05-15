from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import datetime
import calendar
import os

today = datetime.date.today()
uploaded_list = []
if datetime.datetime.today().weekday() == 0:
    next_monday = today
    next_saturday = today + datetime.timedelta(days=5 - today.weekday(), weeks=0)

else:
    next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    next_saturday = today + datetime.timedelta(days=5 - today.weekday(), weeks=1)

next_monday_date = str(int(str(next_monday)[-2:]))
next_monday_month = calendar.month_name[int(str(next_monday)[-5:-3])]
next_monday_year = str(next_monday)[:4]


next_saturday_date = str(next_saturday)[-2:]
next_saturday_month = calendar.month_name[int(str(next_saturday)[-5:-3])]
next_saturday_year = str(next_saturday)[:4]

to_write_date = ' Weekly Test (' + next_monday_date + ' '+ next_monday_month+ ' to '+ next_saturday_date+ ' '+ next_saturday_month+' '+ next_saturday_year+')'

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
subs = ['Bank PO', 'JEE Main', 'NEET UG', 'RRB NTPC', 'SSC CGL']
uploaded_list = []


def create_exams(thread_num):


    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    driver.implicitly_wait(3)
    driver.get('http://center3.exampeer.in/admin/index.php')
    driver.find_elements_by_xpath("//input[@name = 'email']")[0].send_keys('prem@exampeer.com')
    driver.find_elements_by_xpath("//input[@name = 'password']")[0].send_keys(12345678)
    driver.find_elements_by_xpath("//input[@value = 'login']")[0].click()


    driver.get('http://center3.exampeer.in/admin/exam.php')

    while True:
        try:
            driver.find_elements_by_xpath('//input[@type="text"]')[0]
            break
        except:
            driver.get('http://center3.exampeer.in/admin/exam.php')
    driver.find_elements_by_xpath("//a[@href = '#add']")[0].click()

    # -----------------------------------------------------------------------------------------------------------
    #  BANK PO
    if thread_num == 0:
        # sub = subs[0]
        Select(driver.find_element_by_xpath('//select[@class="chzn-select select2-offscreen"]')).select_by_value('802')
        Select(driver.find_element_by_xpath('//select[@class="chzn-select"]')).select_by_value('212')
        driver.find_element_by_xpath('//input[@value="749"]').click()
        driver.find_element_by_xpath('//input[@value="71"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[1].send_keys('35')
        driver.find_element_by_xpath('//input[@value="750"]').click()
        driver.find_element_by_xpath('//input[@value="72"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[3].send_keys('35')
        driver.find_element_by_xpath('//input[@value="751"]').click()
        driver.find_element_by_xpath('//input[@value="73"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[5].send_keys('30')
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[6].send_keys(subs[0]+to_write_date)
        driver.find_elements_by_xpath('//input[@class="validate[required] datepicker hasDatepicker"]')[0].click()
        if datetime.datetime.today().weekday() == 0:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            dates = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
            for date in dates:
                if date.text == next_monday_date:
                    date.click()

        driver.find_elements_by_xpath('//input[@name="exam_duration"]')[0].send_keys('60')
        driver.find_elements_by_xpath('//input[@name="passing_percentage"]')[0].send_keys('50')
        driver.find_elements_by_xpath('//input[@name="re_exam_day"]')[0].send_keys('0')
        driver.find_elements_by_xpath('//input[@name="exam_limit"]')[0].send_keys('1')
        driver.find_elements_by_xpath('//input[@name="neg_mark_status"]')[0].click()
        driver.find_elements_by_xpath('//input[@name="negative_marks"]')[0].send_keys('0.25')

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        while True:
            try:
                driver.find_elements_by_xpath('//input[@type="text"]')[0].send_keys(subs[0]+to_write_date)
                break
            except:
                driver.get('http://center3.exampeer.in/admin/exam.php')
        sleep(0.8)
        link0 = driver.find_elements_by_xpath('//a[@style="margin-top:5px"]')[0].get_attribute('href')
        id0 = int(link0.split('=')[-1])
        print(subs[0], ' exam added now adding centers id: ', id0)
        driver.get(link0)
        centers0 = ["Career & Courses", "Competitors Choice", 'Exampeer', 'Institute of Banking Preparation for Selection', 'ITDP Indrapuri', 'Mastermind Coaching Classes', 'National Institute Of Competitive Services,Patna', 'School of Banking', 'Transforming Dreams', 'Vidyalok App']
        driver.find_elements_by_xpath('//input[@name="result_show_on_mail"]')[0].click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

        for center0 in centers0:
            action.send_keys(center0).perform()

            action.send_keys(Keys.ENTER).perform()


        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        sleep(1)
        print(subs[0], ' added centers or successfully created exam completely')

    # -----------------------------------------------------------------------------------------------------------
    #  JEE MAIN
    if thread_num == 1:
        # sub = subs[1]
        Select(driver.find_element_by_xpath('//select[@class="chzn-select select2-offscreen"]')).select_by_value('19517')
        Select(driver.find_element_by_xpath('//select[@class="chzn-select"]')).select_by_value('348')
        driver.find_element_by_xpath('//input[@value="15704"]').click()
        driver.find_element_by_xpath('//input[@value="690"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[1].send_keys('20')
        driver.find_element_by_xpath('//input[@value="691"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[2].send_keys('5')
        driver.find_element_by_xpath('//input[@value="15705"]').click()
        driver.find_element_by_xpath('//input[@value="692"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[4].send_keys('20')
        driver.find_element_by_xpath('//input[@value="693"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[5].send_keys('5')
        driver.find_element_by_xpath('//input[@value="15706"]').click()
        driver.find_element_by_xpath('//input[@value="694"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[7].send_keys('20')
        driver.find_element_by_xpath('//input[@value="695"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[8].send_keys('5')
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[9].send_keys(subs[1]+to_write_date)
        driver.find_elements_by_xpath('//input[@class="validate[required] datepicker hasDatepicker"]')[0].click()
        if datetime.datetime.today().weekday() == 0:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            dates = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
            for date in dates:
                if date.text == next_monday_date:
                    date.click()

        driver.find_elements_by_xpath('//input[@name="exam_duration"]')[0].send_keys('180')
        driver.find_elements_by_xpath('//input[@name="passing_percentage"]')[0].send_keys('40')
        driver.find_elements_by_xpath('//input[@name="re_exam_day"]')[0].send_keys('0')
        driver.find_elements_by_xpath('//input[@name="exam_limit"]')[0].send_keys('1')
        driver.find_elements_by_xpath('//input[@name="neg_mark_status"]')[0].click()
        driver.find_elements_by_xpath('//input[@name="negative_marks"]')[0].send_keys('1.00')

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        while True:
            try:
                driver.find_elements_by_xpath('//input[@type="text"]')[0].send_keys(subs[1]+to_write_date)
                break
            except:
                driver.get('http://center3.exampeer.in/admin/exam.php')
        sleep(0.8)
        link1 = driver.find_elements_by_xpath('//a[@style="margin-top:5px"]')[0].get_attribute('href')
        id1 = int(link1.split('=')[-1])
        print(subs[1], ' exam added now adding centers id: ', id1)
        driver.get(link1)
        centers1 = ['Career & Courses', 'Competitors Choice', 'Eklabhya Classes Pvt. Ltd.', 'Exampeer', 'Mastermind Coaching Classes', 'Medhavi Innovative Classes', 'Sudha Competitives', 'Teaching Everyone  All Exam Test Login call 9418162827,7018224767', 'Transforming Dreams']
        driver.find_elements_by_xpath('//input[@name="result_show_on_mail"]')[0].click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

        for center1 in centers1:
            action.send_keys(center1).perform()

            action.send_keys(Keys.ENTER).perform()

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        sleep(1)
        print(subs[1], ' added centers or successfully created exam completely')

    # -----------------------------------------------------------------------------------------------------------
    #  NEET UG

    if thread_num == 2:
        # sub = subs[2]
        Select(driver.find_element_by_xpath('//select[@class="chzn-select select2-offscreen"]')).select_by_value('19518')
        Select(driver.find_element_by_xpath('//select[@class="chzn-select"]')).select_by_value('350')
        driver.find_element_by_xpath('//input[@value="15707"]').click()
        driver.find_element_by_xpath('//input[@value="696"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[1].send_keys('45')
        driver.find_element_by_xpath('//input[@value="15708"]').click()
        driver.find_element_by_xpath('//input[@value="697"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[3].send_keys('45')
        driver.find_element_by_xpath('//input[@value="15709"]').click()
        driver.find_element_by_xpath('//input[@value="698"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[5].send_keys('90')
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[6].send_keys(subs[2]+to_write_date)
        driver.find_elements_by_xpath('//input[@class="validate[required] datepicker hasDatepicker"]')[0].click()

        if datetime.datetime.today().weekday() == 0:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            dates = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
            for date in dates:
                if date.text == next_monday_date:
                    date.click()

        driver.find_elements_by_xpath('//input[@name="exam_duration"]')[0].send_keys('180')
        driver.find_elements_by_xpath('//input[@name="passing_percentage"]')[0].send_keys('50')
        driver.find_elements_by_xpath('//input[@name="re_exam_day"]')[0].send_keys('0')
        driver.find_elements_by_xpath('//input[@name="exam_limit"]')[0].send_keys('1')
        driver.find_elements_by_xpath('//input[@name="neg_mark_status"]')[0].click()
        driver.find_elements_by_xpath('//input[@name="negative_marks"]')[0].send_keys('1.00')

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()

        while True:
            try:
                driver.find_elements_by_xpath('//input[@type="text"]')[0].send_keys(subs[2] + to_write_date)
                break
            except:
                driver.get('http://center3.exampeer.in/admin/exam.php')
        sleep(0.8)
        link2 = driver.find_elements_by_xpath('//a[@style="margin-top:5px"]')[0].get_attribute('href')
        id2 = int(link2.split('=')[-1])
        print(subs[2], ' exam added now adding centers id: ', id2)
        driver.get(link2)
        centers2 = ['Career & Courses', 'Competitors Choice', 'Eklabhya Classes Pvt. Ltd.', 'Exampeer',
                    'Mastermind Coaching Classes', 'Medhavi Innovative Classes', 'Sudha Competitives',
                    'Teaching Everyone  All Exam Test Login call 9418162827,7018224767', 'Transforming Dreams']

        driver.find_elements_by_xpath('//input[@name="result_show_on_mail"]')[0].click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

        for center2 in centers2:
            action.send_keys(center2).perform()

            action.send_keys(Keys.ENTER).perform()

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        sleep(1)
        print(subs[2], ' added centers or successfully created exam completely')

    # -----------------------------------------------------------------------------------------------------------
    #  RRB NTPC
    if thread_num == 3:
        # sub = subs[3]
        Select(driver.find_element_by_xpath('//select[@class="chzn-select select2-offscreen"]')).select_by_value('19457')
        Select(driver.find_element_by_xpath('//select[@class="chzn-select"]')).select_by_value('307')
        driver.find_element_by_xpath('//input[@value="4334"]').click()
        driver.find_element_by_xpath('//input[@value="524"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[1].send_keys('100')
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[2].send_keys(subs[3]+to_write_date)
        driver.find_elements_by_xpath('//input[@class="validate[required] datepicker hasDatepicker"]')[0].click()
        if datetime.datetime.today().weekday() == 0:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            dates = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
            for date in dates:
                if date.text == next_monday_date:
                    date.click()

        driver.find_elements_by_xpath('//input[@name="exam_duration"]')[0].send_keys('60')
        driver.find_elements_by_xpath('//input[@name="passing_percentage"]')[0].send_keys('50')
        driver.find_elements_by_xpath('//input[@name="re_exam_day"]')[0].send_keys('0')
        driver.find_elements_by_xpath('//input[@name="exam_limit"]')[0].send_keys('1')
        driver.find_elements_by_xpath('//input[@name="neg_mark_status"]')[0].click()
        driver.find_elements_by_xpath('//input[@name="negative_marks"]')[0].send_keys('0.25')

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()

        while True:
            try:
                driver.find_elements_by_xpath('//input[@type="text"]')[0].send_keys(subs[3] + to_write_date)
                break
            except:
                driver.get('http://center3.exampeer.in/admin/exam.php')
        sleep(0.8)
        link3 = driver.find_elements_by_xpath('//a[@style="margin-top:5px"]')[0].get_attribute('href')
        id3 = int(link3.split('=')[-1])
        print(subs[3], ' exam added now adding centers id: ', id3)
        driver.get(link3)
        centers3 = ['Career & Courses', 'Competitors Choice', 'Exampeer', 'Institute of Banking Preparation for Selection ', 'ITDP Indrapuri', 'Mastermind Coaching Classes', 'National Institute Of Competitive Services,Patna', 'School of Banking', 'Transforming Dreams', 'Vidyalok App']

        driver.find_elements_by_xpath('//input[@name="result_show_on_mail"]')[0].click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

        for center3 in centers3:
            action.send_keys(center3).perform()

            action.send_keys(Keys.ENTER).perform()

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        sleep(1)
        print(subs[3], ' added centers or successfully created exam completely')


    # -----------------------------------------------------------------------------------------------------------
    #  SSC CLG
    if thread_num == 4:
        # sub = subs[4]
        Select(driver.find_element_by_xpath('//select[@class="chzn-select select2-offscreen"]')).select_by_value('19455')
        Select(driver.find_element_by_xpath('//select[@class="chzn-select"]')).select_by_value('239')
        driver.find_element_by_xpath('//input[@value="837"]').click()
        driver.find_element_by_xpath('//input[@value="144"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[1].send_keys('25')
        driver.find_element_by_xpath('//input[@value="838"]').click()
        driver.find_element_by_xpath('//input[@value="145"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[3].send_keys('25')
        driver.find_element_by_xpath('//input[@value="839"]').click()
        driver.find_element_by_xpath('//input[@value="146"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[5].send_keys('25')
        driver.find_element_by_xpath('//input[@value="840"]').click()
        driver.find_element_by_xpath('//input[@value="147"]').click()
        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[7].send_keys('25')

        driver.find_elements_by_xpath('//input[@class="validate[required]"]')[8].send_keys(subs[4]+to_write_date)
        driver.find_elements_by_xpath('//input[@class="validate[required] datepicker hasDatepicker"]')[0].click()
        if datetime.datetime.today().weekday() == 0:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
        else:
            dates = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
            for date in dates:
                if date.text == next_monday_date:
                    date.click()

        driver.find_elements_by_xpath('//input[@name="exam_duration"]')[0].send_keys('60')
        driver.find_elements_by_xpath('//input[@name="passing_percentage"]')[0].send_keys('50')
        driver.find_elements_by_xpath('//input[@name="re_exam_day"]')[0].send_keys('0')
        driver.find_elements_by_xpath('//input[@name="exam_limit"]')[0].send_keys('1')
        driver.find_elements_by_xpath('//input[@name="neg_mark_status"]')[0].click()
        driver.find_elements_by_xpath('//input[@name="negative_marks"]')[0].send_keys('0.50')

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()

        while True:
            try:
                driver.find_elements_by_xpath('//input[@type="text"]')[0].send_keys(subs[4] + to_write_date)
                break
            except:
                driver.get('http://center3.exampeer.in/admin/exam.php')
        sleep(0.8)
        link4 = driver.find_elements_by_xpath('//a[@style="margin-top:5px"]')[0].get_attribute('href')
        id4 = int(link4.split('=')[-1])
        print(subs[4], ' exam added now adding centers id: ', id4)
        driver.get(link4)
        centers4 = ['Career & Courses', 'Competitors Choice', 'Exampeer', 'Institute of Banking Preparation for Selection ', 'ITDP Indrapuri', 'Mastermind Coaching Classes', 'National Institute Of Competitive Services,Patna', 'School of Banking', 'Transforming Dreams', 'Vidyalok App']

        driver.find_elements_by_xpath('//input[@name="result_show_on_mail"]')[0].click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

        for center4 in centers4:
            action.send_keys(center4).perform()

            action.send_keys(Keys.ENTER).perform()

        driver.find_elements_by_xpath('//button[@class="btn btn-gray"]')[0].click()
        sleep(1)
        print(subs[4], ' added centers or successfully created exam completely')
    # driver.quit()
    print('all done of', subs[thread_num])
    input('ENTER WHEN DONe')
    # ------------------------------------------------------------------------------------------

    files = os.listdir('ready_excels_weekly')
    file_path = 'C:\\Users\\PRINCE MEHTA\\PycharmProjects\\Rough_automation\\ready_excels_weekly'
    total_files = len(files)

    driver.get('http://center3.exampeer.in/admin/import_table.php')

    for count, file in enumerate(files):
        if file not in uploaded_list:
            uploaded_list.append(file)
            while True:
                try:
                    driver.find_elements_by_xpath("//input[@type='text']")
                    break
                except:
                    driver.get('http://center3.exampeer.in/admin/import_table.php')

            driver.find_elements_by_xpath("//a[@href = '#add']")[0].click()

            driver.find_elements_by_xpath("//input[@type = 'file']")[0].send_keys(file_path + '\\' + file)
            driver.find_elements_by_xpath("//button[@type = 'submit']")[0].click()
            # sleep(3)
            print('uploaded: ', file, count + 1, '/', total_files)
            try:
                name = quote(file)
            except:
                name = str(file)

            driver.get('http://center3.exampeer.in/admin/import.php?import=' + name)
            print('imported: ', file, count + 1, '/', total_files)
    driver.quit()
with ThreadPoolExecutor(max_workers=25) as executor:
    executor.map(create_exams, list(range(5)))

print('ALL DONE')