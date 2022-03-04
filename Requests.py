import requests
import json

url = ("https://api.covid19api.com/live/country/spain/status/confirmed")

response = requests.get(url)
json_data = response.json()
todayStats = json_data[-1]
weekAgoStats = json_data[-8]
twoWeeksAgoStats = json_data[-15]
    
latestStats = todayStats["Active"] - weekAgoStats["Active"]
lastWeekStats = weekAgoStats["Active"] - twoWeeksAgoStats["Active"]

if latestStats < lastWeekStats:
    trend = "Down"
else: 
    trend = "Up"

if latestStats > 1000:
    lockdown = "true"
else:
    lockdown = "false"

dictionary = {
    "cases": todayStats["Confirmed"] - weekAgoStats["Confirmed"],
    "active": todayStats["Active"] - weekAgoStats["Active"],
    "trend": trend,
    "lockdown": lockdown
}

with open("corona-data.json", "w") as file:
    json.dump(dictionary, file)






