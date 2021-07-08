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

        sql = """
            SELECT subs.name, subs.code as userid
            FROM sale_subscription as subs,
            sale_subscription_line as line
            WHERE subs.partner_id IN (
                select id
                from res_partner
                where res_partner.location IS NOT NULL
            )
            AND subs.atm_ref IS NOT NULL 
            AND subs.stage_id IN (
                SELECT id
                FROM sale_subscription_stage
                WHERE name = 'Draft'
            ) 
        """
        # , line.display_name as offer
        #     AND subs.recurring_invoice_line_ids = line.product_id
            # AND subs.partner_id = (yung nagtrigger)


        self.env.cr.execute(sql)
        records = self.env.cr.fetchall()

        # Converts result ids to a model object
        # records = model.browse([rec[0] for rec in records])
        _logger.info("Sending SMS to:")
        _logger.info(records)
        _logger.info(("Records Count: %s") % len(records))

        # if records:
        #     params = self.env['ir.config_parameter'].sudo()
        #     aradial_url = params.get_param('aradial_url')
        #     aradial_token = params.get_param('aradial_token')

        #     user = AradialAPIGateway(
        #         url=aradial_url,
        #         token=aradial_token
        #         , records = records
        #     )
        #     created_user = user.create_user()

        #     _logger.info(created_user)
        