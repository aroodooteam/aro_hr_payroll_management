# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _
from openerp.exceptions import Warning, ValidationError
import logging
_logger = logging.getLogger(__name__)

class HrPayrollRubrique(models.Model):
    _name = 'hr.payroll.rubrique'
    _description = 'Gestion des rubriques'
    
    code_rubrique = fields.Char(string='Code rubrique')
    name = fields.Char(string='Nom de la rubrique')
    category_id = fields.Many2one('hr.salary.rule.category',string=u'Catégorie')


class HrPayrollRubriqueLine(models.Model):
    _name = 'hr.payroll.rubrique.line'
    _description = 'Detail des rybrique'

    employee_contract_id = fields.Many2one('hr.contract',string=u'Référence Contrat')
    rubrique_id = fields.Many2one('hr.payroll.rubrique',string='Rubrique')
    code_rubrique = fields.Char(string='Code rubrique',related='rubrique_id.code_rubrique',store=True)
    amount = fields.Float(string='Montant')

    @api.multi
    def name_get(self):
        result = super(HrPayrollRubriqueLine,self).name_get()
        res = []
        print("result = %s" % result)
        for rec in result:
            # rec = (rec.id,  r_name)
            el_obj = self.browse(rec[0])
            #r_name = rec[1] + ' '+ '[' + el_obj.annee + ']'+ ' '+ '[' + el_obj.employee_id.name.name + ']'
            r_name = '[' + el_obj.rubrique_id.name + ']'+' '+ rec[1] + ' '+ '[' + el_obj.code_rubrique + ']'
            res.append((el_obj.id,  r_name))
        return res

#class HrPayrollRubriqueList(models.Model):
    #_name = 'hr.payroll.list.rubrique'
    #_description = 'Champs rubrique'

    #complement_salaire = fields.Float(string='COMPLEMENT SALAIRE',digits=(16, 2))
    #indemnite_representation = fields.Float(string='INDEMNITE REPRES',digits=(16, 2))
    #rembousement_avance = fields.Float(string='REMBOURSEMENT AVANCE',digits=(16, 2))
    #retraite_prevoyance = fields.Float(string='RETRAITE ET PREVOYANCE',digits=(16, 2))
    #cotisation_amicale = fields.Float(string='COTISATION AMICALE',digits=(16, 2))
    #cotisation_medicale = fields.Float(string='COTISATION SERVICE MEDICALE',digits=(16, 2))

