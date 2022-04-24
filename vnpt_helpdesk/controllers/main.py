from odoo import http
from odoo.http import request
import logging
import traceback
from werkzeug.exceptions import BadRequest, InternalServerError

_logger = logging.getLogger(__name__)


class VnptHelpDeskController(http.Controller):

    @http.route("/bptoday/api/location", type='json', auth='public')
    def api_bptd_location(self, **kwargs):
        if request.httprequest.method == 'POST':
            try:
                location = request.env['bptd.location'].sudo().api_create_location(data=request.jsonrequest)
            except KeyError as e:
                err_msg = traceback.format_exc()
                _logger.error(err_msg)
                raise BadRequest("Missing required field: %s" % e)
            except Exception:
                err_msg = traceback.format_exc()
                _logger.error(err_msg)
                raise InternalServerError("An exception occurred during an http request")
            return location.parse_data()
        else:
            raise BadRequest("Invalid request method")
