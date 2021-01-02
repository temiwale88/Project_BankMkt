import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''
# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
              "age": "57",
              "job": "technician",
              "marital": "married",
              "education": "high.school",
              "default": "no",
              "housing": "no",
              "loan": "yes",
              "contact": "cellular",
              "month": "may",
              "day_of_week": "mon",
              "duration": "371",
              "campaign": "1",
              "pdays": "999",
              "previous": "1",
              "poutcome": "failure",
              "emp.var.rate": "-1.8",
              "cons.price.idx": "92.89299999999999",
              "cons.conf.idx": "-46.2",
              "euribor3m": "1.2990000000000002",
              "nr.employed": "5099.1",
              "y": "no"
            },
            {
              "age": "55",
              "job": "unknown",
              "marital": "married",
              "education": "unknown",
              "default": "unknown",
              "housing": "yes",
              "loan": "no",
              "contact": "telephone",
              "month": "may",
              "day_of_week": "thu",
              "duration": "285",
              "campaign": "2",
              "pdays": "999",
              "previous": "0",
              "poutcome": "nonexistent",
              "emp.var.rate": "1.1",
              "cons.price.idx": "93.994",
              "cons.conf.idx": "-36.4",
              "euribor3m": "4.86",
              "nr.employed": "5191.0",
              "y": "no"
            },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


