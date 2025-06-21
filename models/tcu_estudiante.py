from odoo import models, fields


class TCUEstudiante(models.Model):
    _name = 'tcu.estudiante'
    _description = 'Estudiante TCU'

    name = fields.Char(string='Nombre Completo', required=True)
    identificacion = fields.Char(string='Identificación')
    carnet = fields.Char(string='Carnet Universitario')
    correo = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    lugar_tcu = fields.Char(string='Lugar donde realizará el TCU')
    encargado = fields.Char(string='Nombre del Encargado')
    fecha_solicitud = fields.Date(string='Fecha de Solicitud')

    estado_solicitud = fields.Selection([
        ('en_revision', 'En Revisión'),
        ('pendiente', 'Pendiente'),
        ('rechazado', 'Rechazado'),
        ('aprobado', 'Aprobado'),
    ], string='Estado de la Solicitud', default='pendiente')

    observaciones = fields.Text(string='Observaciones')
    carta_aceptacion = fields.Binary(string='Carta de Aceptación')
    documento_adicional = fields.Binary(string='Documento Adicional')


    def enviar_estado_por_correo(self):
        for estudiante in self:
            template = self.env.ref('modulo_tcu.email_template_estado_solicitud')
            if template:
                template.send_mail(estudiante.id, force_send=True)

    def accion_cambiar_estado(self):
        """Modifica el estado de la solicitud y envía una notificación por correo."""
        for rec in self:
            if rec.estado_solicitud == 'pendiente':
                rec.estado_solicitud = 'en_revision'
            elif rec.estado_solicitud == 'en_revision':
                rec.estado_solicitud = 'aprobado'
            elif rec.estado_solicitud == 'rechazado':
                rec.estado_solicitud = 'pendiente'

            # Enviar notificación por correo después del cambio de estado
            rec.enviar_estado_por_correo()

