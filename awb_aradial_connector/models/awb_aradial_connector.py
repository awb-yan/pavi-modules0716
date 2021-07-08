from ..api.aradial_gateway.create_user import AradialAPIGateway
from odoo import api, fields, models, exceptions, _
from psycopg2.extensions import AsIs
import datetime
import logging

_logger = logging.getLogger(__name__)

class AWBAradialConnector(models.Model):

    _name = 'awb.aradial.connector'
    _description = 'AWB Aradial Connector'


    def create_user(self):

        # sql = select name, partner_id from sale.subsription
        #   where subscriber_location_id is not null 
        #   and atm_ref is not null 
        #   and subscription_status === draft 
        #   and partner_id = (yung nagtrigger)
        # execute (sql)
        # records = fetchall()

        # kung records.length > 0
        #   continue process


        params = self.env['ir.config_parameter'].sudo()
        aradial_url = params.get_param('aradial_url')
        aradial_token = params.get_param('aradial_token')

        user = AradialAPIGateway(
            url=aradial_url,
            token=aradial_token
            # , records = records
        )
        created_user = user.create_user()

        _logger.info(created_user)
        