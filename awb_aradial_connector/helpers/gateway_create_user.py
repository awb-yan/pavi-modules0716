import json
import requests
from odoo import exceptions


class AradialAPIGateway(object):
    def __init__(
        self
    ):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic QVBJVXNlcjpwYXNzd29yZA=='   #TODO: hard-coded
        }

        self.url = 'http://172.16.101.2/api/users'              #TODO: hard-coded

    def create_user_in_aradial(
        self
    ):
        data = {                                                #TODO: hard-coded
            'UserID': 'user6',
            'Password': 'password',
            'Offer': 'Unlimited'
        }

        try:
            res = requests.post(
                url=self.url,
                headers=self.headers,
                data=json.dumps(data)
            )
        except requests.exceptions.MissingSchema as e:
            raise exceptions.ValidationError(e)
        return res

    def create_user(self):
        res = self.create_user_in_aradial()
        state = "created" if res.status_code == 201 else "failed"

        return state

