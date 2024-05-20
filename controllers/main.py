from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
import logging

_logger = logging.getLogger(__name__)

class SignupController(Home):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        print("web_auth_signup called")
        res = super(SignupController, self).web_auth_signup(*args, **kw)
        try:
            ils = request.env['agd.il'].sudo().search([])
            print("ILS:", ils)
            res.qcontext.update({
                'ils': ils
            })
        except Exception as e:
            print("Error fetching ils:", str(e))
        return res

    @http.route('/get_districts', type='json', auth='public', website=True)
    def get_districts(self, il_id):
        try:
            il_id = int(il_id)
            print("Getting districts for il_id:", il_id)
            districts = request.env['agd.ilce'].sudo().search([('il_id', '=', il_id)])
            print("Districts:", districts)
            return [{'id': d.id, 'name': d.name} for d in districts]
        except Exception as e:
            print("Error in get_districts:", e)
            return {'error': str(e)}

    @http.route('/get_schools', type='json', auth='public', website=True)
    def get_schools(self, ilce_id):
        try:
            ilce_id = int(ilce_id)
            print("Getting schools for ilce_id:", ilce_id)
            schools = request.env['agd.lise'].sudo().search([('ilce_id', '=', ilce_id)])
            print("Schools:", schools)
            return [{'id': s.id, 'name': s.name} for s in schools]
        except Exception as e:
            print("Error in get_schools:", e)
            return {'error': str(e)}
