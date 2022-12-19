from odoo import _, api, fields, models


class   Crmteamoinhertit(models.Model):
    _inherit = "crm.team"

    crm_team_comer = fields.Monetary("Marge")
    crm_team_chif = fields.Monetary("Chiffre d'affaire")
    crm_team_N_client = fields.Integer("Nombre de clients")
    crm_team_N_contrat= fields.Integer("Nombre de contrats")




















