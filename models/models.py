from odoo import models, fields, api

class Il(models.Model):
    _name = 'agd.il'
    _description = 'Il'

    name = fields.Char(string='Name', required=True)
    ilce_ids = fields.One2many('agd.ilce', 'il_id', string='İlçeler')
    lise_ids = fields.One2many('agd.lise', 'il_id', string='Liseler')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'il_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    @api.depends('user_ids')
    def _compute_user_count(self):
        for il in self:
            il.user_count = len(il.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'İldeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree',
            'domain': [('il_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }

class Ilce(models.Model):
    _name = 'agd.ilce'
    _description = 'Ilce'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('agd.il', string='İl', required=True)
    lise_ids = fields.One2many('agd.lise', 'ilce_id', string='Liseler')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'ilce_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    @api.depends('user_ids')
    def _compute_user_count(self):
        for ilce in self:
            ilce.user_count = len(ilce.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'İlçedeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree,form',
            'view_id': self.env.ref('agd.view_ilce_users_tree').id,
            'domain': [('ilce_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }

class Lise(models.Model):
    _name = 'agd.lise'
    _description = 'Lise'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('agd.il', string='İl', required=True)
    ilce_id = fields.Many2one('agd.ilce', string='İlçe')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'lise_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    @api.depends('user_ids')
    def _compute_user_count(self):
        for lise in self:
            lise.user_count = len(lise.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lisedeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree,form',
            'domain': [('lise_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }
