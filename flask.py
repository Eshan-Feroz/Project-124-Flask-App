  
from flask import Flask,jsonify, request

app = Flask(__name__)

Tasks = [
    {
        'id': 1,
        'Name': u'Eshan',
        'Contact': u'7392598267', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Jason',
        'Contact': u'9279563814', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Provide the valid data: "
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    Tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : Tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)