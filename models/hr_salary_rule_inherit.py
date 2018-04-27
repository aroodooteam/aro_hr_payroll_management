# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _
from openerp.exceptions import Warning, ValidationError
import logging
_logger = logging.getLogger(__name__)


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    _description = 'Lier les regles salariales aux contrats'

    #contract_id = fields.Many2one('hr.contract',string=u'Référence contrat')


    

