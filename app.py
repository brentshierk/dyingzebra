#imports
from flask import Flask, render_template, redirect,url_for,jsonify,request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
driver.get("https://www.gradescope.com/")
find_login_button = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button').click()
driver.implicitly_wait(15)
send_login_username = driver.find_element_by_xpath('//*[@id="session_email"]').send_keys('brent.shierk@students.makeschool.com')
send_login_password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('bls24511289!')
click_login_button = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div[1]/form/div[4]/input').click()
driver.implicitly_wait(15)

#begining to scrape data class name
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
#get due date //*[@id="assignments-student-table"]/tbody/tr[1]/td[2]/div/div[3]/span[2]
get_assignment_dueDate =driver.find_element_by_xpath('//*[@id="assignments-student-table"]/tbody/tr[1]/td[2]/div/div[3]/span[2]').get_attribute('innerHTML')
print(get_assignment_dueDate)
driver.quit()

#app config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/" ,methods=['GET','POST'])


@app.route('/ping', methods=['GET'])
def ping_pong():
    
    return jsonify('pong!!')


@app.route('/Books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]
    


if __name__ == '__main__':
    app.run()