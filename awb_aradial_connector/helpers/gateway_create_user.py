import json
import requests
from odoo import exceptions


class AradialAPIGateway(object):
    def __init__(
        self,
        url,
        token
    ):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        self.url = url

    def create_user_in_aradial(
        self
    ):
        data = {                                    #TODO: hard-coded
            'UserID': 'user6',                      #subscription id from Odoo
            'Password': 'password',                 #system generated?
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
        # get UserId, password and Offer here before calling create_user_in_aradial()
         
        res = self.create_user_in_aradial()
        state = "created" if res.status_code == 201 else "failed"

        return state
