import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendacerealtime-62d17-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "321654":{
        "name": "xyz",
        "major": "ai",
        "starting_year": 2021,
        "total_attendance":6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-11-29 00:54:34"
    },
"852741":{
        "name": "girl",
        "major": "ai",
        "starting_year": 2021,
        "total_attendance":10,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-11-29 00:54:34"
    },
"963852":{
        "name": "boy",
        "major": "ai",
        "starting_year": 2021,
        "total_attendance":5,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-11-29 00:54:34"
    },
"123456":{
        "name": "boys",
        "major": "ai",
        "starting_year": 2021,
        "total_attendance":60,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2023-11-29 00:54:34"
    },
"1by21ai002":{
        "name": "boys123",
        "major": "ai",
        "starting_year": 2021,
        "total_attendance":62,
        "standing": "G",
        "year": 5,
        "last_attendance_time": "2023-11-29 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)