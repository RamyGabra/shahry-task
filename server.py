from flask import Flask
from flask import request
import datetime


app = Flask(__name__)

# Unique 14 digit number
# 0    -->  centuary
# 1-6  -->  date of birth
# 7-8  -->  district
# 9-13 -->  serial number (odd=Male, Even=Female)
# 14   -->  check sum digit

# governerates code mapping
governorates = {'01': 'Cairo',
                '02': 'Alexandria',
                '03': 'Port Said',
                '04': 'Suez',
                '11': 'Damietta',
                '12': 'Dakahlia',
                '13': 'Ash Sharqia',
                '14': 'Kaliobeya',
                '15': 'Kafr El - Sheikh',
                '16': 'Gharbia',
                '17': 'Monoufia',
                '18': 'El Beheira',
                '19': 'Ismailia',
                '21': 'Giza',
                '22': 'Beni Suef',
                '23': 'Fayoum',
                '24': 'El Menia',
                '25': 'Assiut',
                '26': 'Sohag',
                '27': 'Qena',
                '28': 'Aswan',
                '29': 'Luxor',
                '31': 'Red Sea',
                '32': 'New Valley',
                '33': 'Matrouh',
                '34': 'North Sinai',
                '35': 'South Sinai',
                '88': 'Foreign' } 


def extract_birthdate(national_id):

    first_digit = int(national_id[0:1])
    century = first_digit*100 + 1700
    
    year = int(national_id[1:3]) + century
    month = int(national_id[3:5])
    day = int(national_id[5:7])

    birthdate = datetime.date(year, month, day)

    return birthdate


def extract_governorate(national_id):
    governorate_code = national_id[7:9]
    try: 
        governorate = governorates[governorate_code]
    except:
        governorate = "invalid"

    return governorate    


def extract_gender(national_id):
    gender_digit = int(national_id[13:14])
    if gender_digit % 2 == 0:
        gender='Female'
    else:
        gender='Male' 

    return gender


@app.route("/extract_info", methods=['POST'])
def extract_info():
    body = request.get_json()
    national_id = body['national_id']

    # check length of national id
    if len(national_id) != 14 or not national_id.isnumeric():
        return {"national_id": national_id, "is_valid": False, "date": None, "governorate": None, "gender": None}

    # If invalid birthdate then national id is invalid
    try:
        birthdate = extract_birthdate(national_id)
    except Exception:
        return {"national_id": national_id, "is_valid": False, "date": None, "governorate": None, "gender": None}
    
    governorate = extract_governorate(national_id)

    # if birthdate is greater than today's date or invalid govrenorate code then invalid
    if governorate == "invalid" or birthdate > datetime.datetime.now().date(): 
        return {"national_id": national_id, "is_valid": False, "date": None, "governorate": None, "gender": None}
    
    gender = extract_gender(national_id)

    return {"national_id": national_id, "is_valid": True, "date": birthdate, "governorate": governorate, "gender": gender}
    
