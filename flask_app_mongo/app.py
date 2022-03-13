from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
from flask_mde import Mde


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.flask_db
notes = db.notes
mde = Mde(app)
    
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        note_title = request.form['content']
        notes.insert_one({'title': note_title,"jots":[], "createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()})
        return redirect(url_for('index'))
        
    all_notes = notes.find().sort("updatedAt", -1)
    return render_template('index.html', all_notes=all_notes)

@app.route('/delete/<id>')
def delete(id):
    notes.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    note = notes.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        new_note_title = request.form['content']
        notes.update_one({"_id": ObjectId(id)}, {"$set": {"updatedAt": datetime.datetime.now(), "title":new_note_title}})
        return redirect(url_for('index'))
    else:
        return render_template('update.html', note=note)
    
@app.route('/insert/<id>', methods=['GET', 'POST'])
def insert(id):
    note = notes.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        new_jot_content = request.form['content']
        # notes.update_one({"_id": ObjectId(id)}, {"$set": {"updatedAt": datetime.datetime.now(), "title":new_note_title}})
        notes.update_one({"_id": ObjectId(id)}, {"$push": {"jots":{"jot_content":new_jot_content}}}) 
        return redirect(url_for('index'))
    else:
        return render_template('insert.html', note=note)
    

if __name__ == '__main__':
    app.run(debug=True)