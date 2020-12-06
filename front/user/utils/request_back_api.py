import requests
import json
import urllib


class BackEnd():

    def get_user(self):
        #TODO: Change this at Deployment for the Heroku address
        url = 'http://localhost:5000/user'

        response = requests.post(url)
        r = response.json()
        return r
        #return response.json()
