from odoo import api, fields, models
from odoo.exceptions import UserError

class BptdLocation(models.Model):
    _name = "bptd.location"
    _description = "Binh Phuoc Today Location Management"

    uuid = fields.Char('Device UUID')
    latitude = fields.Char('Latitude')
    longitude = fields.Char('Longitude')
    platform = fields.Selection([('ios', 'IOS'),
                                 ('android', 'Android')], string="Device Type")

    @api.model
    def _api_prepare_create_vals(self, data):
        return {
            'uuid': data["uuid"],
            'latitude': data["latitude"],
            'longitude': data["longitude"],
            'platform': data["platform"],
        }

    @api.model
    def api_create_location(self, data):
        vals = self._api_prepare_create_vals(data)
        record = self.create(vals)
        return record

    def parse_data(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'platform': self.platform,
        }
