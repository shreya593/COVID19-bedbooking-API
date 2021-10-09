from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,  request
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/COVID19"

mongo = PyMongo(app)


@app.route('/Bookbed', methods=['POST'])
def add_user():
    _json = request.json
    _patientcriticallevel = _json['patient_critical_level']
    _pincode = _json['pincode']
    _hospital = _json['hospital']
    _timeslot = _json['timeslot']
    
    if _patientcriticallevel and  _pincode and  _hospital and _timeslot and request.method =='POST':
        id = mongo.db.Bedbooking.insert({'patient_critical_level': _patientcriticallevel, 'pincode': _pincode, 'hospital': _hospital, 'timeslot': _timeslot})
        resp = jsonify("Bed Booked Successfully")
        resp.status_code = 200
        return resp
    else:
        return  not_found()    




@app.route('/Bedlist')
def Bedlist():
    Bedlist = mongo.db.Bedbooking.find()
    resp = dumps(Bedlist)
    return resp

@app.route('/Cancelbooking/<id>',methods=['DELETE'])
def cancelbooking(id):
    mongo.db.Bedbooking.delete_one({'_id':ObjectId(id)})
    resp = jsonify("Booking Cancelled")

    resp.status_code = 200

    return resp


@app.route('/Reschedule/<id>',methods=['PUT'])
def reschedule(id):
    _id = id
    _json = request.json
    _patientcriticallevel = _json['patient_critical_level']
    _pincode = _json['pincode']
    _hospital = _json['hospital']
    _timeslot = _json['timeslot']

    if _patientcriticallevel and  _pincode and  _hospital and _timeslot and request.method =='PUT':
        id = mongo.db.Bedbooking.update_one({ '_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set': {'patient_critical_level': _patientcriticallevel,'pincode': _pincode, 'hospital': _hospital, 'timeslot': _timeslot}})
        resp = jsonify("Bedbooking Rescheduled Successfully")
        resp.status_code = 200
        return resp
    else:
        return  not_found() 
    


@app.errorhandler(404)
def not_found(error=None):
    message= {
        'status': 404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp



if __name__ == "__main__":
    app.run(debug=True)


