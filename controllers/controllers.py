# -*- coding: utf-8 -*-
# from odoo import http


# class Agd(http.Controller):
#     @http.route('/agd/agd', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agd/agd/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agd.listing', {
#             'root': '/agd/agd',
#             'objects': http.request.env['agd.agd'].search([]),
#         })

#     @http.route('/agd/agd/objects/<model("agd.agd"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agd.object', {
#             'object': obj
#         })
