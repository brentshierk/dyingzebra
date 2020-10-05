from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#selenium config
DRIVER_PATH = '/Users/brent/Desktop/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://youtube.com')

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#this first function goes to gradescope and logs into my account
#def login_gradescope():
driver.get("https://www.gradescope.com/")
find_login_button = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button').click()
driver.implicitly_wait(15)
send_login_username = driver.find_element_by_xpath('//*[@id="session_email"]').send_keys('brent.shierk@students.makeschool.com')
send_login_password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('bls24511289!')
click_login_button = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div[1]/form/div[4]/input').click()
driver.implicitly_wait(15)

#begining to scrape data class name
#def get_assignment_data():
first_class = driver.find_element_by_xpath('//*[@id="account-show"]/div[1]/div/a[1]').click()
find_class_name = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/header/h1').get_attribute('innerHTML').splitlines()[0]
className = find_class_name
print(className)

#scraping first assignment 
   
get_assignments = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/th/a').get_attribute('innerHTML')

print(get_assignments)
    
#assignment status
get_assignment_status = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/td[1]/div[2]').get_attribute('innerHTML')
print(get_assignment_status)

#get due date 
get_assignment_dueDate = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/td[2]/div/div[3]/span[2]').get_attribute('innerHTML')
print(get_assignment_dueDate)

driver.quit()



#login_gradescope()
#get_assignment_data()
