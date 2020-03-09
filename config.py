"""Config File"""
#! fill in needed information

#dict {'url': price}
to_track = {}

RECIPIENT = "EMAIL_FOR_RECIPIENT"
#Interval when to check for priceupdate
TRACK_TIME = 60*60

#account details for sending email
SENDER = "EMAIL_FOR_SENDER"
PASSWORD = "PASSWORD_FOR_SENDER"

JSON_FILE = 'tracker_json.txt'

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

SMTPSERVER = 'smtp.gmail.com'
PORT = 587
