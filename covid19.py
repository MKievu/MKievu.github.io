
import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
import pync
import time
#let there is no data initially
def update():
    url = "https://api.coronatracker.com/v5/analytics/newcases/country?countryCode=VN&startDate=2021-08-23&endDate=2021-08-25"
    covidData = requests.get(url)
    data = covidData.json()        
    #repeating the loop for multiple times
    while(True):
        pync.notify(
            title = "Dạ thưa ông chủ San Công Tử",
            message = f"Số ca nhiễm  :{data[0]['new_infections']}\nSố ca tử vong hôm nay:{data[0]['new_deaths']}\nSố ca hồi phục hôm nay:{data[0]['new_recovered']}" 
        )
        time.sleep(10
)
        #sleep for 4 hrs => 60*60*4 sec
        #notification repeats after every 4hr

if __name__ == '__main__':  
    update()