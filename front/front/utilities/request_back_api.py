import requests
import json


class BackEndServiceConnection():

    #TODO: Change this at Deployment for the Heroku address
    url = 'http://localhost:5000/'


    def post(self, endpoint):
        url = self.url + endpoint 

        response = requests.post(url)
        return response.json()

    def get(self, endpoint):
        url = self.url + endpoint 

        response = requests.get(url)
        return response.json()
