#scraper broken

# from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from flask import Flask, render_template, redirect,url_for,jsonify,request
# from flask_cors import CORS
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId

# DEBUG = True

# app = Flask(__name__)
# app.config.from_object(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
# mongo = PyMongo(app)

# #selenium config
# DRIVER_PATH = '/Users/brent/Desktop/chromedriver'


# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# #this first function goes to gradescope and logs into my account
# #def login_gradescope():
# driver.get("https://www.gradescope.com/")
# find_login_button = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button').click()
# driver.implicitly_wait(15)
# send_login_username = driver.find_element_by_xpath('//*[@id="session_email"]').send_keys('brent.shierk@students.makeschool.com')
# send_login_password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('bls24511289!')
# click_login_button = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div[1]/form/div[4]/input').click()
# driver.implicitly_wait(15)

# #begining to scrape data class name
# #def get_assignment_data():
# first_class = driver.find_element_by_xpath('//*[@id="account-show"]/div[1]/div/a[1]').click()
# find_class_name = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/header/h1').get_attribute('innerHTML').splitlines()[0]
# className = find_class_name
# print(className)

# #scraping first assignment 
   
# get_assignments = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/th/a').get_attribute('innerHTML')

# print(get_assignments)
    
# #assignment status
# get_assignment_status = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/td[1]/div[2]').get_attribute('innerHTML')
# print(get_assignment_status)

# #get due date 
# get_assignment_dueDate = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/td[2]/div/div[3]/span[2]').get_attribute('innerHTML')
# print(get_assignment_dueDate)





# #login_gradescope()
# #get_assignment_data()





# table = driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody')
# i = 1
# #scrape gradescope for assignment names 
# # while table.find_element_by_xpath(f'.//tr[{i}]') is not None:
# #     assignment_names = []
# #     row = table.find_element_by_xpath(f'.//tr[{i}]')
# #     assignment_names.append(([a.text for a in row.find_elements_by_xpath('.//th/a')]))
# #     i += 1
# #     if i == 10:
# #         print('end of loop')
# #         break
# #     #print([a.text for a in row.find_elements_by_xpath('.//th/a')])
# #     print(assignment_names)

    
# # # //*[@id="assignments-student-table"]/tbody/tr[1]/th/a
# # # //*[@id="assignments-student-table"]/tbody/tr[2]/th/a

# # scrape for assignment grade status 
# # while table.find_element_by_xpath(f'.//tr[{i}]') is not None:
# #     grades = []
# #     row = table.find_element_by_xpath(f'.//tr[{i}]')
# #     grades.append(([td.text for td in row.find_elements_by_xpath('.//td[1]')]))
# #     i += 1
# #     if i == 10:
# #         print('end of loop')
# #         break
# #     print(grades)
    
# #scrape for due date of assignment 
# while table.find_element_by_xpath(f'.//tr[{i}]') is not None:
#     due_date =[]
#     row = table.find_element_by_xpath(f'.//tr[{i}]')
#     due_date.append(([td.text for td in row.find_elements_by_xpath('.//td[2]/div/div/span[2]')]))
#     i += 1
#     if i == 10:
#         print('end of loop')
#         break
#     print(due_date)
# #print(get_dueDate(due_date))
# #print(due_date)

    
# #//*[@id="assignments-student-table"]/tbody/tr[1]/td[2]/div/div/span[2]

   