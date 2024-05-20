from odoo import models, fields, api

class Il(models.Model):
    _name = 'agd.il'
    _description = 'Il'

    name = fields.Char(string='Name', required=True)
    ilce_ids = fields.One2many('agd.ilce', 'il_id', string='İlçeler')
    lise_ids = fields.One2many('agd.lise', 'il_id', string='Liseler')


class Ilce(models.Model):
    _name = 'agd.ilce'
    _description = 'Ilce'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('agd.il', string='İl', required=True)
    lise_ids = fields.One2many('agd.lise', 'ilce_id', string='Liseler')


class Lise(models.Model):
    _name = 'agd.lise'
    _description = 'Lise'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('agd.il', string='İl', required=True)
    ilce_id = fields.Many2one('agd.ilce', string='İlçe')

    @api.onchange('il_id')
    def _onchange_il_id(self):
        if self.il_id:
            return {'domain': {'ilce_id': [('il_id', '=', self.il_id.id)]}}
        else:
            self.ilce_id = False
            return {'domain': {'ilce_id': [('id', '=', False)]}}
