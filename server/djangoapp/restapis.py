import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
def get_request(url, params):
    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'}, auth=HTTPBasicAuth('apikey', "zbYqiP-zFDseJSxDxZYIiHbEDD7PRQXPgBZknVU-D6-8"))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
def post_request(url, payload):   
    return requests.post(url,  json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, params):
    f = open('/home/project/ibmCapstone/cloudant/data/dealerships.json')
    data = json.load(f)
    f.close()
    return data
    #dealers = get_request(url, params)
    #return dealers #possibly .text if .json() doesn't work
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list

def get_dealers_by_state(state):
    f = open('/home/project/ibmCapstone/cloudant/data/dealerships.json')
    data = json.load(f)
    f.close()
    rlist = {'dealerships':[]}
    for dealership in data['dealerships']:
        if dealership['st'] == state:
            rlist['dealerships'].append(dealership)
    return rlist

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_reviews_by_id_from_cf(dealer_id):
    f = open('/home/project/ibmCapstone/cloudant/data/reviews-full.json')
    data = json.load(f)
    f.close()
    rlist = {'reviews':[]}
    for review in data['reviews']:
        if review['dealership'] == dealer_id:
            rlist['reviews'].append(review)
    return rlist['reviews']
    #dealers = get_request(url, {"dealer":dealerId})
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list

def post_review(payload):
    f = open('/home/project/ibmCapstone/cloudant/data/reviews-full.json')
    data = json.load(f)
    data['reviews'].append(payload)
    f.write(data)
    f.close()

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



