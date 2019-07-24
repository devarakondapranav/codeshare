from flask import Flask, jsonify
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect("db.sqlite3", check_same_thread = False)
print(connection)

@app.route('/')
def home():
	return "codeshare home"



@app.route('/<int:artid>')
def hello_world(artid):

	cursor = connection.execute("Select * from snippets_code LIMIT 1 OFFSET " + str(artid))
	row = cursor.fetchone()
	
	d = {}
	d["title"] = row[4]
	d["author"] = row[2]
	d["pub_date"] = row[3]
	d["id"] = row[0]
	
	return jsonify(d)

	
@app.route('/length')
def yo():
	cursor = connection.execute("Select COUNT(*) from snippets_code")
	row = cursor.fetchone()
	return jsonify({'length':row[0]})



if __name__ == '__main__':
   app.run(host = "0.0.0.0", port="5001", debug=True)
