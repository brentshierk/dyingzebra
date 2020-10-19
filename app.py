#imports
from flask import Flask, render_template, redirect,url_for,jsonify,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


#app config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project"
mongo = PyMongo(app)

@app.route('/')
def assignment_list():

    assignments_data = mongo.db.assignments.find({})
    print(assignments_data)
    

    context = {
        'assignments': assignments_data,
    }
    return render_template('assignment_list.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        new_assignment = {
            'class_name': request.form.get('class_name'),
            'assignment_name': request.form.get('assignment_name'),
            'due_date':request.form.get('due_date'),
            'submit_status': request.form.get('submit_status'),
            'submission_link': request.form.get('submission_link')
        }
      
        result = mongo.db.assignments.insert_one(new_assignment)
        inserted_id = result.inserted_id
        return  redirect(url_for('detail', assignment_id=inserted_id))

    else:
        return render_template('create.html')

@app.route('/assignments/<assignment_id>')
def detail(assignment_id):

    assignment_to_show = mongo.db.assignments.find_one({'_id':ObjectId(assignment_id)})
    
    print(assignment_id)
   
    grades = list(mongo.db.grades.find({'assignment_id':assignment_id}))
    

    context = {
        'assignment' : assignment_to_show,
        'grades': grades,
        'assignment_id': assignment_id
    }

    print(assignment_to_show)
    return render_template('detail.html', **context)
    

@app.route('/grades/<assignment_id>', methods=['POST'])
def grades(assignment_id):
    
    new_grade = {
        'grade': request.form.get('grade_score'), 
        'date': request.form.get('due_date'),
        'assignment_id': assignment_id
    }
    
 
    update_grade = mongo.db.grades.insert_one(new_grade)

    return redirect(url_for('detail', assignment_id=assignment_id))

@app.route('/edit/<assignment_id>', methods=['GET', 'POST'])
def edit(assignment_id):
    if request.method == 'POST':
        
        new_assignment = {
            'class_name': request.form.get('class_name'),
            'assignment_name': request.form.get('assignment_name'),
            'due_date':request.form.get('due_date') ,
            'submit_status': request.form.get('submit_status'),
            'submission_link': request.form.get('submission_link')
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