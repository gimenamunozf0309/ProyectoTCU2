from odoo import http
from odoo.http import request
from odoo.fields import Date

class TCUEstudianteAPI(http.Controller):

    @http.route('/api/info_estudiante', type='json', auth='public', methods=['GET'], csrf=False)
    def get_estudiante(self, **kw):
        cedula = kw.get('cedula')
        estudiante = request.env['res.partner'].sudo().search([('identification_id', '=', cedula)], limit=1)
        if estudiante:
            return {
                'nombre': estudiante.name,
                'correo': estudiante.email,
                'cedula': estudiante.identification_id,
                'telefono': estudiante.phone,
            }
        return {}

    @http.route('/api/periodo_activo', type='json', auth='public', methods=['GET'], csrf=False)
    def get_periodo(self):
        periodo = request.env['tcu.periodo'].sudo().search([('activo', '=', True)], limit=1)
        if periodo:
            return {
                'id': periodo.id,
                'name': periodo.name,
                'año': periodo.anno
            }
        return {}

    @http.route('/api/crear_solicitud', type='json', auth='public', methods=['POST'], csrf=False)
    def crear_solicitud(self, **post):
        valores = {
            'name': post.get('nombre'),
            'identificacion': post.get('cedula'),
            'correo': post.get('correo'),
            'carnet': post.get('carnet'),
            'telefono': post.get('telefono'),
            'lugar_tcu': post.get('lugar_tcu'),
            'encargado': post.get('encargado'),
            'fecha_solicitud': Date.today(),
            'estado_solicitud': 'pendiente',
        }
        nueva = request.env['tcu.estudiante'].sudo().create(valores)
        return {'success': True, 'id': nueva.id}