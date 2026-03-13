import requests
import smtplib

my_email = "favourhenrytest@gmail.com"
password = "htglcwuknrvflocw"
r_email =  "favourhenrytest@yahoo.com"

api_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "b6427eaaf03fb6f4fae376ab81b6e903"
parameters = {
    "lat": 44.389339,
    "lon": -79.685516,
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

# print(weather_data)

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



# print(codes)
# print("Bring Umbrella")
