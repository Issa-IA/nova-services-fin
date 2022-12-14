from odoo import _, api, fields, models
import warnings


class Aficherlalistecontacts(models.Model):
    _name = 'afichercontacts'
    _description = ' client fleet seriel article'
    comercial_contact_affiche = fields.Boolean(default=False,string="Afficher la liste des contacts")
    comercial_contact_retirer = fields.Boolean(default=False, string="Masquer la liste des contacts")

    def name_get(self):
        result = []
        for model in self:
            name = "Afficher ou masquer la liste des contacts"
            result.append((model.id, name))
        return result

    @api.onchange("comercial_contact_affiche")
    def onchange_affiche(self):
        print("bonjour tout le monde")
        your_group = self.env.ref('affiche_comerciaux_contact.acces_contact_user')
        users = self.env['res.users'].search([])
        users_Technicien = self.env.ref('droits_d_acces.group_Technicien_contact').users.ids
        print("users", users)
        print("users_Technicien",users_Technicien)

        for user in users:
            if users_Technicien:
                if user.id in users_Technicien:
                    your_group.write({
                        'users': [(4, user.id)]
                    })

        warning = {'title': _("Contacts"),
                       'message': 'La liste des contacts est disponible pour les commerciaux',
                    }
        return {'warning': warning}


    @api.onchange("comercial_contact_retirer")
    def onchange_retirer(self):
        print("bonjour tout le monde")
        your_group = self.env.ref('affiche_comerciaux_contact.acces_contact_user')
        users = self.env['res.users'].search([])
        users_Technicien = self.env.ref('droits_d_acces.group_Technicien_contact').users.ids
        for user in users:
            if users_Technicien:
                if user.id in users_Technicien:
                    your_group.write({
                        'users': [(3, user.id)]
                    })
        warning = {
                        'title': _("Contacts"),
                        'message': 'La liste des contacts a été retiré pour les commerciaux',
                    }
        return {'warning': warning}




