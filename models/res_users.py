from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    il_id = fields.Many2one('agd.il', string='Province')
    ilce_id = fields.Many2one('agd.ilce', string='District')
    lise_id = fields.Many2one('agd.lise', string='School')

    managed_il_ids = fields.One2many('agd.il', 'manager_id', string='Yönettiği İller')
    managed_ilce_ids = fields.One2many('agd.ilce', 'manager_id', string='Yönettiği İlçeler')
    managed_lise_ids = fields.One2many('agd.lise', 'manager_id', string='Yönettiği Liseler')

    def action_grant_karma(self):
        self.ensure_one()
        self.karma += 10  # Örneğin, 10 karma puanı ekleyin
