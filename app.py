#imports
from flask import Flask, render_template, redirect,url_for,jsonify,request
#from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

"""
adding comment block
"""
#app config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)
#CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def assignment_list():
    """Display the plants list page."""

    assignments_data = mongo.db.assignments.find({})
    print(assignments_data)
    

    context = {
        'assignments': assignments_data,
    }
    return render_template('assignment_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    if request.method == 'POST':
        
        new_assignment = {
            'class_name': request.form.get('class_name'),
            'assignment_name': request.form.get('assignment_name'),
            'due_date':request.form.get('due_date'),
            'submit_status': request.form.get('submit_status'),
        }
      
        result = mongo.db.assignments.insert_one(new_assignment)
        inserted_id = result.inserted_id
        return  redirect(url_for('detail', assignment_id=inserted_id))

    else:
        return render_template('create.html')

@app.route('/assignments/<assignment_id>')
def detail(assignment_id):
    """Display the plant detail page & process data from the harvest form."""

    assignment_to_show = mongo.db.assignments.find_one({'_id':ObjectId(assignment_id)})
    
    print(assignment_id)
   
    grades = list(mongo.db.grades.find({'assignment_id':assignment_id}))
    # for harvest in harvests:
    #     print(harvest)
    

    context = {
        'assignment' : assignment_to_show,
        'grades': grades,
        'assignment_id': assignment_id
    }

    print(assignment_to_show)
    return render_template('detail.html', **context)
    

@app.route('/grades/<assignment_id>', methods=['POST'])
def grades(assignment_id):
    """
    Accepts a POST request with data for 1 harvest and inserts into database.
    """
    new_grade = {
        'grade': request.form.get('grade_score'), # e.g. '3 tomatoes'
        'date': request.form.get('due_date'),
        'assignment_id': assignment_id
    }
    
 
    update_grade = mongo.db.grades.insert_one(new_grade)

    return redirect(url_for('detail', assignment_id=assignment_id))

@app.route('/edit/<assignment_id>', methods=['GET', 'POST'])
def edit(assignment_id):
    """Shows the edit page and accepts a POST request with edited data."""
    if request.method == 'POST':
        
        new_assignment = {
            'class_name': request.form.get('class_name'),
            'assignment_name': request.form.get('assignment_name'),
            'due_date':request.form.get('due_date') ,
            'submit_status': request.form.get('submit_status')
        }
        
        mongo.db.assignments.update_one({'_id':ObjectId(assignment_id)},{'$set':new_assignment})

        
        return redirect(url_for('detail', assignment_id=assignment_id))
    else:
       
        assignment_to_show = mongo.db.assignments.find_one({'_id':ObjectId(assignment_id)})
        print('---')
        print(assignment_to_show)

        context = {
            'assignment': assignment_to_show
        }

        return render_template('edit.html', **context)

@app.route('/delete/<assignment_id>', methods=['POST'])
def delete(assignment_id):
   
    mongo.db.assignment.delete_one({'_id':ObjectId(assignment_id)})

    
    mongo.db.grades.delete_many({'_id':ObjectId(assignment_id)})

    return redirect(url_for('assignment_list'))

if __name__ == '__main__':
    app.run(debug=True)