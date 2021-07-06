from ..helpers.gateway_create_user import AradialAPIGateway
from odoo import api, fields, models, exceptions, _
from psycopg2.extensions import AsIs
import datetime
import logging

_logger = logging.getLogger('AWB-Aradial')

class UserCreation(models.Model):

    def user_creation(self):
        _name = 'awb.aradial.connector'
        _description = 'AWB Aradial Connector'


        params = self.env['ir.config_parameter'].sudo()
        aradial_url = params.get_param('aradial_url')
        aradial_token = params.get_param('aradial_token')

        user = AradialAPIGateway(
            url=aradial_url,
            token=aradial_token
        )
        created_user = user.create_user()
        _logger = logging.getLogger(created_user)
        