# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _
from openerp.exceptions import Warning, ValidationError
import logging
_logger = logging.getLogger(__name__)

class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Rajout de champs rubriques dans la tabale contrat'

    contract_rubrique_ids = fields.One2many('hr.payroll.rubrique.line','employee_contract_id',string='Rubriques')
    carte_nom = fields.Float(string='CARTE NOM',digits=(16, 2))
    rappel_base = fields.Float(string='RAPPEL BASE',digits=(16, 2))
    rappel_assiduite = fields.Float(string='RAPPEL ASSIDUITE',digits=(16, 2))
    rappel_anciennete = fields.Float(string='RAPPEL ANCIENNETE',digits=(16, 2))
    rappel_indemnite_repres = fields.Float(string='RAPPEL INDEMNITE DE REPRESENTATION',digits=(16, 2))
    rappel_indemnite_transp = fields.Float(string='RAPPEL INDEMNITE DE TRANSPORT',digits=(16, 2))
    rappel_indemnite_fonction = fields.Float(string='RAPPEL INDEMNITE DE FONCTION',digits=(16, 2))
    rappel_prime_technicite = fields.Float(string='RAPPEL PRIME DE TECHNICITE',digits=(16, 2))
    prime_efficience = fields.Float(string='PRIME D EFFICIENCE',digits=(16, 2))
    heure_sup = fields.Float(string='HEURES SUPPLEMENTAIRES',digits=(16, 2))
    prime_rendement = fields.Float(string='PRIME DE RENDEMENT',digits=(16, 2))
    prime_assiduite = fields.Float(string='PRIME D ASSIDUITE',digits=(16, 2))
    indemnite_stage = fields.Float(string='INDEMNITE DE STAGE',digits=(16, 2))
    indemnite_caisse = fields.Float(string='INDEMNITE DE CAISSE',digits=(16, 2))
    indemnite_interim = fields.Float(string='INDEMNITE D\'INTERIM',digits=(16, 2))
    gratification = fields.Float(string='GRATIFICATION',digits=(16, 2))
    participation_benef = fields.Float(string='PARTICIPATION BENEFICIARE',digits=(16, 2))
    rembt_epargne = fields.Float(string='REMBOURSEMENT EPARGNE',digits=(16, 2))
    indemnite_de_preavis = fields.Float(string='INDEMNITE DE PREAVIS',digits=(16, 2))
    complement_salaire = fields.Float(string='COMPLEMENT SALAIRE',digits=(16, 2))
    indemnite_representation = fields.Float(string='INDEMNITE DE REPRESENTATION',digits=(16, 2))
    remboursement_avance = fields.Float(string='REMBOURSEMENT AVANCE',digits=(16, 2))
    retraite_prevoyance = fields.Float(string='RETRAITE ET PREVOYANCE',digits=(16, 2))
    cotisation_amicale = fields.Float(string='COTISATION AMICALE',digits=(16, 2))
    cotisation_medicale = fields.Float(string='COTISATION SERVICE MEDICALE',digits=(16, 2))
    indemnite_logement = fields.Float(string='INDEMNITE DE LOGEMENT',digits=(16, 2))
    indemnite_transport = fields.Float(string='INDEMNITE DE TRANSPORT',digits=(16, 2))