from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.flask_db
notes = db.notes

notes.insert_one({'title':"Test Note",
                  "jots":[{"jot_content":"first jot"},{"jot_content":"second jot"}],
                  "createdAt": datetime.datetime.now(), 
                  "updatedAt": datetime.datetime.now()})
