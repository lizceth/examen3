from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from django.conf import settings

class Profile(models.Model):
    SELECT=(
        ('dni','dni'),
        ('pass.','pasaporte'),
        ('Tr.mil','tarjeta militar'),
    )
    usuario=models.OneToOneField(User)
    telefono=models.IntegerField()
    documento=models.CharField(max_length=7, choices=SELECT)
    numero_doc=models.CharField(max_length=8)
    departamento=models.CharField(max_length=20)
    distrito =models.CharField(max_length=20)
    provincia =models.CharField(max_length=20)
    zona_horaria=TimeZoneField(default='America/Lima')
    class Meta:
        permissions=(
            ('create','puede crear'),
            ('list','listar'),
            ('view','puede ver'),
            ('update','puede actualizar'),
            ('delete','puede eliminar'),
        )
    def __unicode__(self):
        return self.documento

@models.permalink
def get_absolute_url(self):
    return ('detail', [int(self.pk)])
