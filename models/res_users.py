from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    il_id = fields.Many2one('agd.il', string='Province', store=True)
    ilce_id = fields.Many2one('agd.ilce', string='District', store=True)
    lise_id = fields.Many2one('agd.lise', string='School', store=True)

    adres = fields.Char(string="Adres", store=True)
    birth_date = fields.Date(string="Doğum Günü", store=True)
    birth_place = fields.Char(string="Doğum Yeri", store=True)
    school_email = fields.Char(string="Okul Email", store=True)
    twitter_account = fields.Char(string="Twitter", store=True)
    facebook_account = fields.Char(string="Facebook", store=True)
    instagram_account = fields.Char(string="Instagram", store=True)
    linkedin_account = fields.Char(string="LinkedIn", store=True)
    uni_id = fields.Many2one('agd.uni', string='Üniversite', store=True)
    fak_id = fields.Many2one('agd.fak', string='Fakülte', store=True)
    bolum_id = fields.Many2one('agd.bolum', string='Bölüm', store=True)
    managed_il_ids = fields.One2many('agd.il', 'manager_id', string='Yönettiği İller', store=True)
    managed_ilce_ids = fields.One2many('agd.ilce', 'manager_id', string='Yönettiği İlçeler', store=True)
    managed_lise_ids = fields.One2many('agd.lise', 'manager_id', string='Yönettiği Liseler', store=True)
    nationality_id = fields.Many2one('res.country', string='Uyruk', store=True)
    tc_kimlik_no = fields.Char(string="Tc Kimlik No", store=True)
    gender = fields.Selection([
        ('male', 'Erkek'),
        ('female', 'Kadın'),
    ], string='Cinsiyet', store=True)

    @api.model
    def create(self, vals):
        res = super(ResUsers, self).create(vals)
        if 'partner_id' in vals:
            partner = res.partner_id
            partner.adres_yeni = res.adres
            partner.birth_date_yeni = res.birth_date
            partner.birth_place_yeni = res.birth_place
            partner.school_email_yeni = res.school_email
            partner.twitter_account_yeni = res.twitter_account
            partner.facebook_account_yeni = res.facebook_account
            partner.instagram_account_yeni = res.instagram_account
            partner.linkedin_account_yeni = res.linkedin_account
            partner.uni_id_yeni = res.uni_id
            partner.fak_id_yeni = res.fak_id
            partner.bolum_id_yeni = res.bolum_id
            partner.managed_il_ids_yeni = res.managed_il_ids
            partner.managed_ilce_ids_yeni = res.managed_ilce_ids
            partner.managed_lise_ids_yeni = res.managed_lise_ids
            partner.nationality_id_yeni = res.nationality_id
            partner.tc_kimlik_no_yeni = res.tc_kimlik_no
            partner.gender_yeni = res.gender
        return res

    def write(self, vals):
        res = super(ResUsers, self).write(vals)
        for user in self:
            if user.partner_id:
                partner_vals = self._prepare_partner_vals(user)
                user.partner_id.write(partner_vals)
        return res

    def _prepare_partner_vals(self, user):
        partner_vals = {
            'adres_yeni': user.adres,
            'birth_date_yeni': user.birth_date,
            'birth_place_yeni': user.birth_place,
            'school_email_yeni': user.school_email,
            'twitter_account_yeni': user.twitter_account,
            'facebook_account_yeni': user.facebook_account,
            'instagram_account_yeni': user.instagram_account,
            'linkedin_account_yeni': user.linkedin_account,
            'uni_id_yeni': user.uni_id,
            'fak_id_yeni': user.fak_id,
            'bolum_id_yeni': user.bolum_id,
            'managed_il_ids_yeni': user.managed_il_ids,
            'managed_ilce_ids_yeni': user.managed_ilce_ids,
            'managed_lise_ids_yeni': user.managed_lise_ids,
            'nationality_id_yeni': user.nationality_id,
            'tc_kimlik_no_yeni': user.tc_kimlik_no,
            'gender_yeni': user.gender,
        }
        return partner_vals

    @api.constrains('tc_kimlik_no')
    def _check_tc_kimlik_no(self):
        for record in self:
            if record.tc_kimlik_no:
                if not record.tc_kimlik_no.isdigit():
                    raise ValidationError('TC Kimlik No sadece rakamlardan oluşmalıdır.')
                if len(record.tc_kimlik_no) != 11:
                    raise ValidationError('TC Kimlik No 11 haneli olmalıdır.')

    def action_grant_karma(self):
        self.ensure_one()
        self.karma += 10  # Örneğin, 10 karma puanı ekleyin
