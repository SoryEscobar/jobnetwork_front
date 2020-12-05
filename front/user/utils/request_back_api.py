import requests


class BackEnd():

    def get_user(self):
        #TODO: Change this at Deployment for the Heroku address
        url = 'http://localhost:5000/user'

        response = requests.get(url)
        return response.json()
