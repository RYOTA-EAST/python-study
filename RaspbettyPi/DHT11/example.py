""" 
温度と湿度を取得して
スプレッドシートに記録
温度が基準を超えると
slackに通知する

温湿度センサDHT11のライブラリを以下のコマンドで取得して
git clone https://github.com/szazo/DHT11_Python.git
同名ファイルを置き換える
"""


import requests
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import slackweb, config


# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
status = 0

slack = slackweb.Slack(url = config.slack_url)
google_sheet_url = config.google_sheet_url

try:
    while True:
        result = instance.read()
        if result.is_valid():
            temperaturedata = result.temperature
            humiditydata = result.humidity
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            
            if status == 0 and temperaturedata > 30:
                print("temp hot!")
#                 slack.notify(text="rasPi hot!!!")
                status = 1
                
            if status == 1 and temperaturedata < 28:
                print("temp cold")
                status = 0


            url = f'{google_sheet_url}?temperature={temperaturedata}&humidity={humiditydata}'
            requests.get(url)
            
            time.sleep(5)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()