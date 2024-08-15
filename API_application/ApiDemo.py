from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/getData/<id>")
def getData(id):
    d={
        "id":id,
        "name":"Default",
        "email":"abc@gmail.com"
    }
    return jsonify(d),200

@app.route("/createStudent",methods=["POST"])
def createStudent():
    data = request.get_json()
    print(data)
    return "data added",200

app.run()