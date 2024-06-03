from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request

class CustomAuthSignup(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        response = super(CustomAuthSignup, self).web_auth_signup(*args, **kw)
        if response.qcontext.get('error'):
            return response

        # Kullanıcı oluşturulduktan sonra phone alanını güncelle
        user = request.env['res.users'].sudo().search([('login', '=', kw.get('login'))], limit=1)
        if user:
            user.sudo().write({'phone': kw.get('phone')})

        return response
