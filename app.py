import urllib.request
import json

# import Flask
from flask import Flask

# create a Flask app
# to run python3 app.py
app = Flask(__name__)

# establish a Flask route so that we can serve HTTP traffic on that route
# GET api is endpoint/reports/tag_of_data_array
# return JSON with data with all value of "data_field" (example "Titolo") where data_field exist

@app.route('/reports/<data_field>', methods=['GET'])
def reports(data_field):
    i=0
    data = urllib.request.urlopen("https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json").read()
    file_data = json.loads(data)
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    newlist = []
    newlist1 = []
    while i < len(file_data):
        if data_field in file_data[i]['issue']['data'] and "Descrizione" in file_data[i]['issue']['data']:
            newlist.append(file_data[i]['issue']['data']["Descrizione"]) 
            newlist1.append(file_data[i]['issue']['data'][data_field])
        i += 1
    data_set = [{'Description': country, str(data_field): wins} for country, wins in zip(newlist, newlist1)]
    return json.dumps(data_set)
    
#all reports
@app.route('/reports/', methods=['GET'])
def reports_all():
    i=0
    data = urllib.request.urlopen("https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json").read()
    file_data = json.loads(data)
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    newlist = []
    while i < len(file_data):
        #print(file_data[i]['issue']['data'][data_field])
        newlist.append(file_data[i]['issue']['data'])
        i += 1
    return json.dumps(newlist)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to the Covid19Italia.Help API !</h1>"

# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
# data master here https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json
if __name__ == '__main__':
     # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)