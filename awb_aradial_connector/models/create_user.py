from ..helpers.gateway_create_user import AradialAPIGateway
from odoo import api, fields, models, exceptions, _
from psycopg2.extensions import AsIs
import datetime
import logging

_logger = logging.getLogger('AWB-Aradial')

class UserCreation(models.Model):

    def user_creation(self):
        # TODO: hard-coded in the helper class. need to change
        # params = self.env['ir.config_parameter'].sudo()
        # sms_gateway = params.get_param('smart_gateway')
        # sms_gateway_url = params.get_param('smart_gateway_url')
        # sms_gateway_token = params.get_param('smart_gateway_token')
        user = AradialAPIGateway()
        created_user = user.create_user()
        _logger = logging.getLogger(created_user)
        