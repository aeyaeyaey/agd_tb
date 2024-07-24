from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    from odoo import models, fields

    class ResPartner(models.Model):
        _inherit = 'res.partner'

        adres_yeni = fields.Char(string="Adres")
        birth_date_yeni = fields.Date(string="Doğum Günü")
        birth_place_yeni = fields.Char(string="Doğum Yeri")
        school_email_yeni = fields.Char(string="Okul Email")
        twitter_account_yeni = fields.Char(string="Twitter")
        facebook_account_yeni = fields.Char(string="Facebook")
        instagram_account_yeni = fields.Char(string="Instagram")
        linkedin_account_yeni = fields.Char(string="LinkedIn")
        uni_id_yeni = fields.Many2one('agd.uni', string='Üniversite')
        fak_id_yeni = fields.Many2one('agd.fak', string='Fakülte')
        bolum_id_yeni = fields.Many2one('agd.bolum', string='Bölüm')
        managed_il_ids_yeni = fields.One2many('agd.il', 'manager_id', string='Yönettiği İller')
        managed_ilce_ids_yeni = fields.One2many('agd.ilce', 'manager_id', string='Yönettiği İlçeler')
        managed_lise_ids_yeni = fields.One2many('agd.lise', 'manager_id', string='Yönettiği Liseler')
        nationality_id_yeni = fields.Many2one('res.country', string='Uyruk')
        tc_kimlik_no_yeni = fields.Char(string="Tc Kimlik No")
        gender_yeni = fields.Selection([
            ('male', 'Erkek'),
            ('female', 'Kadın'),
        ], string='Cinsiyet')

    @api.depends('user_ids')
    def _compute_user_fields(self):
        for partner in self:
            user = partner.user_ids and partner.user_ids[0] or False
            if user:
                partner.adres = user.adres
                partner.birth_date = user.birth_date
                partner.birth_place = user.birth_place
                partner.school_email = user.school_email
                partner.twitter_account = user.twitter_account
                partner.facebook_account = user.facebook_account
                partner.instagram_account = user.instagram_account
                partner.linkedin_account = user.linkedin_account
                partner.uni_id = user.uni_id
                partner.fak_id = user.fak_id
                partner.bolum_id = user.bolum_id
                partner.nationality_id = user.nationality_id
                partner.tc_kimlik_no = user.tc_kimlik_no
                partner.gender = user.gender
