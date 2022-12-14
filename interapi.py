import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/translate-api', methods=['POST'])
def translate_api():
    # Get the request data
    data = request.get_json()

    # Extract the parameters from the request data
    params = data.get('params')

    # Make a request to the other API using the 'requests' library
    response = requests.get('http://other-api.com/endpoint', params=params)

    # Return the response from the other API to the request originator
    return response.json()

#This will send a POST request with a JSON payload containing
# the parameters for the request to the other API to the
# /translate-api endpoint on the localhost. The API will then make the request to the other API using the specified parameters and return the response to the request originator.


##curl -X POST -H "Content-Type: application/json" -d '{"params": {"param1": "value1", "param2": "value2"}}' http://localhost:5000/translate-api
