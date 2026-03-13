import requests
import smtplib
import os

my_email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")
r_email =  os.environ.get("RECEIVERS_EMAIL")

api_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OW_API_KEY")
parameters = {
    "lat": 9.081999 ,
    "lon": 8.675277,
    "appid": api_key,
    "cnt": 4,
}
# lat = 9.081999
# long = 8.675277
#
# response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}")

response = requests.get(url= api_endpoint, params= parameters)
response.raise_for_status()
weather_data = response.json()


codes = []
will_rain = False

for num in range(0,4):
    code = weather_data["list"][num]["weather"][0]["id"]
    codes.append(code)
    if code < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr= my_email, to_addrs= r_email, msg="Subject:Rain Alert\n\nThere will be rain today, take an umbrella.")




