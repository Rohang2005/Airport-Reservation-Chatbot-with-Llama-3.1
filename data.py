import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("Firebasekey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aoop-46569-default-rtdb.asia-southeast1.firebasedatabase.app/' 
})

flights_data = {
    "IndiGo": {
        "flight_001": {
            "flight_number": "6E101",
            "destination": "Delhi",
            "type": "domestic",
            "price": 150,
            "availability": True
        },
        "flight_002": {
            "flight_number": "6E102",
            "destination": "Mumbai",
            "type": "domestic",
            "price": 200,
            "availability": True
        },
        "flight_003": {
            "flight_number": "6E103",
            "destination": "Bangalore",
            "type": "domestic",
            "price": 220,
            "availability": True
        },
        "flight_004": {
            "flight_number": "6E104",
            "destination": "Kolkata",
            "type": "domestic",
            "price": 180,
            "availability": True
        },
        "flight_005": {
            "flight_number": "6E105",
            "destination": "Hyderabad",
            "type": "domestic",
            "price": 210,
            "availability": False
        },
        "flight_006": {
            "flight_number": "6E106",
            "destination": "Chennai",
            "type": "domestic",
            "price": 190,
            "availability": True
        }
    },
    "Vistara": {
        "flight_007": {
            "flight_number": "UK201",
            "destination": "Delhi",
            "type": "domestic",
            "price": 160,
            "availability": True
        },
        "flight_008": {
            "flight_number": "UK202",
            "destination": "Pune",
            "type": "domestic",
            "price": 230,
            "availability": True
        },
        "flight_009": {
            "flight_number": "UK203",
            "destination": "Jaipur",
            "type": "domestic",
            "price": 175,
            "availability": True
        },
        "flight_010": {
            "flight_number": "UK204",
            "destination": "Goa",
            "type": "domestic",
            "price": 240,
            "availability": True
        },
        "flight_011": {
            "flight_number": "UK205",
            "destination": "Lucknow",
            "type": "domestic",
            "price": 150,
            "availability": False
        },
        "flight_012": {
            "flight_number": "UK206",
            "destination": "Ahmedabad",
            "type": "domestic",
            "price": 200,
            "availability": True
        }
    },
    "Air India": {
        "flight_013": {
            "flight_number": "AI301",
            "destination": "Delhi",
            "type": "domestic",
            "price": 180,
            "availability": True
        },
        "flight_014": {
            "flight_number": "AI302",
            "destination": "Chennai",
            "type": "domestic",
            "price": 220,
            "availability": True
        },
        "flight_015": {
            "flight_number": "AI303",
            "destination": "Bangalore",
            "type": "domestic",
            "price": 210,
            "availability": True
        },
        "flight_016": {
            "flight_number": "AI304",
            "destination": "Hyderabad",
            "type": "domestic",
            "price": 205,
            "availability": False
        },
        "flight_017": {
            "flight_number": "AI305",
            "destination": "Kolkata",
            "type": "domestic",
            "price": 190,
            "availability": True
        },
        "flight_018": {
            "flight_number": "AI306",
            "destination": "Mumbai",
            "type": "domestic",
            "price": 240,
            "availability": True
        }
    },
    "Emirates": {
        "flight_019": {
            "flight_number": "EK501",
            "destination": "Dubai",
            "type": "international",
            "price": 600,
            "availability": True
        },
        "flight_020": {
            "flight_number": "EK502",
            "destination": "New York",
            "type": "international",
            "price": 1200,
            "availability": True
        },
        "flight_021": {
            "flight_number": "EK503",
            "destination": "London",
            "type": "international",
            "price": 800,
            "availability": True
        },
        "flight_022": {
            "flight_number": "EK504",
            "destination": "Toronto",
            "type": "international",
            "price": 950,
            "availability": False
        },
        "flight_023": {
            "flight_number": "EK505",
            "destination": "Paris",
            "type": "international",
            "price": 850,
            "availability": True
        },
        "flight_024": {
            "flight_number": "EK506",
            "destination": "Singapore",
            "type": "international",
            "price": 700,
            "availability": True
        }
    },
    "Qatar Airways": {
        "flight_025": {
            "flight_number": "QR701",
            "destination": "Doha",
            "type": "international",
            "price": 550,
            "availability": True
        },
        "flight_026": {
            "flight_number": "QR702",
            "destination": "London",
            "type": "international",
            "price": 900,
            "availability": True
        },
        "flight_027": {
            "flight_number": "QR703",
            "destination": "New York",
            "type": "international",
            "price": 1100,
            "availability": True
        },
        "flight_028": {
            "flight_number": "QR704",
            "destination": "Bangkok",
            "type": "international",
            "price": 650,
            "availability": False
        },
        "flight_029": {
            "flight_number": "QR705",
            "destination": "Sydney",
            "type": "international",
            "price": 1200,
            "availability": True
        },
        "flight_030": {
            "flight_number": "QR706",
            "destination": "Paris",
            "type": "international",
            "price": 800,
            "availability": True
        }
    },
    "Lufthansa": {
        "flight_031": {
            "flight_number": "LH901",
            "destination": "Frankfurt",
            "type": "international",
            "price": 700,
            "availability": True
        },
        "flight_032": {
            "flight_number": "LH902",
            "destination": "Munich",
            "type": "international",
            "price": 750,
            "availability": True
        },
        "flight_033": {
            "flight_number": "LH903",
            "destination": "Chicago",
            "type": "international",
            "price": 1000,
            "availability": True
        },
        "flight_034": {
            "flight_number": "LH904",
            "destination": "Toronto",
            "type": "international",
            "price": 900,
            "availability": False
        },
        "flight_035": {
            "flight_number": "LH905",
            "destination": "Dubai",
            "type": "international",
            "price": 850,
            "availability": True
        },
        "flight_036": {
            "flight_number": "LH906",
            "destination": "Amsterdam",
            "type": "international",
            "price": 780,
            "availability": True
        }
    }
}

flights_ref = db.reference('flights')
flights_ref.set(flights_data)
print("Flight data added to the Realtime Database.")
