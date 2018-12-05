import json
from json2table import convert
import requests
from gbdx_auth import gbdx_auth

# GET https://rda.geobigdata.io/v1/stripMetadata/4b077271-648e-47fc-a3aa-e01faac7eef1-inv
# results = requests.get('https://geobigdata.io/accounts/v1/accounts?limit=100&page={}'.format(page),headers=headers).json()

# Option 1: Supply bearer token in 'Authorizaton' HTTP header
#
# Users may supply their bearer token using the common oauth2 method that utilizes the 'Authorization' HTTP header.
# Example Authorization HTTP Header: Authorization: Bearer <your bearer token>
# Option 2: 'token' Query Parameter
#
# Users may also supply their bearer token via an HTTP query parameter on the request url.
# Example URL with Query Parameter: https://rda.geobigdata.io/v1/operator?token=<your bearer token>


#Authenticate
s = gbdx_auth.get_session()

#Get the bearer token from the session
parameters = {'token': s.access_token}

#make our request
#resp = requests.get('https://rda.geobigdata.io/v1/stripMetadata/4b077271-648e-47fc-a3aa-e01faac7eef1-inv', params=parameters)

#This is now for working on Operators
operator_resp = requests.get("https://rda.geobigdata.io/v1/operator?fullListing=true", params=parameters)

operator_json = json.loads(operator_resp.content)
operator_json_dict = {"operators": operator_json}
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%", "border": "1px solid black" }

html = convert(operator_json_dict, build_direction=build_direction, table_attributes=table_attributes)

with open('./operators.html', 'w') as f:
    f.write(html)

print('done')


