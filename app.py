from flask import Flask, redirect, render_template, url_for, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://am07:Atiq&mussu07@students-cluster.8lvrhup.mongodb.net/?retryWrites=true&w=majority")

db = client.Alfesani_Solution_Limited
collction = db.Emp_info

@app.route('/')
def index():

    empRecords = collction.find()
    return render_template("index.html", empRecords=empRecords)

@app.route('/insertEmp', methods=['POST', 'GET'])
def insert():
    if request.method=="POST":
        empName= request.form["empName"]
        empDept= request.form["empDept"]
        empGender= request.form.get("empGender")
        empIntro= request.form["empIntro"]
        print(empName, empIntro, empDept, empGender)

        empRecord = {"Name": empName, "Department": empDept, "Gender": empGender, "Introduction": empIntro }
        collction.insert_one(empRecord)
        return redirect("/")
    return redirect("/")

@app.route("/deleteEmp/<_id>", methods=['POST', 'GET'])
def delete(_id):
    collction.delete_one({"_id":ObjectId(_id)})
    return redirect('/')

@app.route('/update/<_id>', methods=["GET", "POST"])
def updateEmp(_id):
    update_id = _id
    return render_template("update.html", _id=update_id)

@app.route("/updateEmp", methods=["GET", "POST"])
def update():
     if request.method=="POST":
        _id= request.form["empID"]
        empName= request.form["empName"]
        empDept= request.form["empDept"]
        empGender= request.form.get("empGender")
        empIntro= request.form["empIntro"]
        collction.update_one({"_id": ObjectId(_id)}, {"$set":{"Name":empName, "Department":empDept, "Gender":empGender, "Introduction":empIntro}})
        return redirect("/")
    
if __name__=="__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)