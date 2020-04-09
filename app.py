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

@app.route('/reports/<data_field>')
def reports(data_field):
    i=0
    data = urllib.request.urlopen("https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json").read()
    file_data = json.loads(data)
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    newlist = []
    while i < len(file_data):
        if data_field in file_data[i]['issue']['data']:
            #print(file_data[i]['issue']['data'][data_field])
            newlist.append(file_data[i]['issue']['data'][data_field])
        i += 1
    return json.dumps(newlist)


# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
# data master here https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json
if __name__ == '__main__':
    app.run(debug=True)