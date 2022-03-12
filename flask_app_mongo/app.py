from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.flask_db
notes = db.notes
    
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        note_content = request.form['content']
        notes.insert_one({'content': note_content,"createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()})
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
        new_note_content = request.form['content']
        notes.update_one({"_id": ObjectId(id)}, {"$set": {"updatedAt": datetime.datetime.now(), "content":new_note_content}})
        return redirect(url_for('index'))
    else:
        return render_template('update.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)