from django.db import models

class PeriodoTCU(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del período
    fecha_inicio = models.DateField()  # Fecha de inicio
    fecha_fin = models.DateField()  # Fecha de fin
    estado = models.CharField(max_length=20, choices=[
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
        ('Pendiente', 'Pendiente')
    ])

    def __str__(self):
        return f"{self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"

class TCUEstudiante(models.Model):
    nombre = models.CharField(max_length=100)  # Name
    identificacion = models.CharField(max_length=20)  # identificacion
    carnet = models.CharField(max_length=20)  # Carnet
    correo = models.EmailField()  # correo
    telefono = models.CharField(max_length=15)  # Teléfono

    #### Relación con PeriodoTCU
    periodo_tcu = models.ForeignKey(PeriodoTCU, on_delete=models.CASCADE)  # 🔹 Agregar esta línea

    #### Control de la solicitud
    lugar_tcu = models.CharField(max_length=200)  # ubicacion
    encargado = models.CharField(max_length=100)  # nombre encargado
    fecha_solicitud = models.DateField()  # Fecha
    estado = models.CharField(
        max_length=20,
        choices=[
            ('En revisión', 'En revisión'),
            ('Pendiente', 'Pendiente'),
            ('Rechazado', 'Rechazado'),
            ('Aprobado', 'Aprobado')
        ],
        default='Pendiente'
    )  # Estado
    observaciones = models.TextField(blank=True)  # Comentarios
    documento = models.FileField(upload_to='documentos_tcu/', blank=True, null=True)  # Para enviar carta

    def __str__(self):
        return f"{self.nombre} - {self.estado}"