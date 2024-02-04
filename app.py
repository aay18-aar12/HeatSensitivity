from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<int:page>')
def hello_world(page):

    ko = (page*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')

    return request2.json()


@app.route('/health')
def retHealth():
    return 'Web Service is Working'
