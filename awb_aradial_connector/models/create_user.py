from ..helpers.gateway_create_user import AradialAPIGateway
from odoo import api, fields, models, exceptions, _
from psycopg2.extensions import AsIs
import datetime
import logging

_logger = logging.getLogger(__name__)

class UserCreation(models.Model):

    _name = 'awb.aradial.connect'
    _description = 'AWB Aradial Connector'

    def test_function(self):
        _logger.info('===== Created User =====')
        _logger.info('=====  =====')
        _logger.info('=====  =====')
        _logger.info('=====  =====')
        _logger.info('===== Created User =====')        

    def user_creation(self):

        params = self.env['ir.config_parameter'].sudo()
        aradial_url = params.get_param('aradial_url')
        aradial_token = params.get_param('aradial_token')

        user = AradialAPIGateway(
            url=aradial_url,
            token=aradial_token
        )
        created_user = user.create_user()
        _logger.info('===== Created User =====')
        _logger.info('===== , created_user , =====')
        _logger.info('===== Created User =====')

        _logger.info(created_user)
        