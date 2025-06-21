from odoo import models, fields

class TCUPeriodo(models.Model):
    _name = 'tcu.periodo'
    _description = 'Periodo de TCU'

    name = fields.Char(string='Nombre del Periodo', required=True)
    activo = fields.Boolean(string='Activo')
    año = fields.Char(string='Año')
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_final = fields.Date(string='Fecha Final')
