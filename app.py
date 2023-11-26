from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<int:page>')
def hello_world(page):

    ko = (page*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')

    return request2.json()

@app.route('/poc/<string:p_poc>/<int:page>')
def retPoc(p_poc, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_POC%20%3D%20'+p_poc+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/child/<string:p_child>/<int:page>')
def retChild(p_child, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_POC%20%3D%20'+p_child+'20)%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo


@app.route('/elderly/<string:p_elderly>/<int:page>')
def retElderly(p_elderly, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_ELDERLY%20%3D%20'+p_elderly+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/poverty/<string:p_poverty>/<int:page>')
def retPoverty(p_poverty, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_POVERTY%20%3D%20'+p_poverty+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/disability/<string:p_disability>/<int:page>')
def retDisability(p_disability, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_DISABILITY%20%3D%20'+p_disability+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/limeng/<string:p_limengy>/<int:page>')
def retLimeng(p_limeng, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_LIMENG%20%3D%20%27'+p_limeng+'%27)%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/treecover/<string:p_treecover>/<int:page>')
def retTreecover(p_treecover, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_TREECOVER%20%3D%20'+p_treecover+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/notree/<string:p_notree>/<int:page>')
def retNotree(p_notree, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_NOTREE%20%3D%20'+p_notree+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

@app.route('/impsurf/<string:p_impsurf>/<int:page>')
def retImpsurf(p_impsurf, page):


    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Health_WebMercator/MapServer/32/query?where=%20(P_IMPSURF%20%3D%20'+p_impsurf+')%20&outFields=*&resultOffset='+str(ko)+'&outSR=4326&f=json')
    bo = request.json()
    return bo

app.route('/health')
def retHealth():
    return 'Web Service is Working'
