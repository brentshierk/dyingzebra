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
driver.get("https://www.gradescope.com/")
find_login_button = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button').click()
driver.implicitly_wait(15)
send_login_username = driver.find_element_by_xpath('//*[@id="session_email"]').send_keys('brent.shierk@students.makeschool.com')
send_login_password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('bls24511289!')
click_login_button = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div[1]/form/div[4]/input').click()
driver.implicitly_wait(15)
first_class = driver.find_element_by_xpath('//*[@id="account-show"]/div[1]/div/a[1]').click()
find_class_name = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/header/h1').get_attribute('innerHTML').splitlines()[0]
className = find_class_name
print(className)
driver.quit()
print(className)
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