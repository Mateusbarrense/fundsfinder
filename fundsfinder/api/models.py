import uuid

from django.conf.locale import de
from django.db import models

# Create your models here.


class FundoImobiliario(models.Model):
    SETOR_CHOICES = [
    ('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido',
    'Híbrido'),
    ('lajes_corporativas', 'Lajes Corporativas'),
    ('logistica', 'Logística'), ('outros', 'Outros'),
    ('residencial', 'Residencial'),
    ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')
    ]
    id_fundo_imobiliario = models.UUIDField(primary_key=True, default=uuid.uuid4)
    codigo_fundo_imobiliario = models.CharField(max_length=8, null=False, blank=False)
    setor = models.CharField(max_length=100, null=False, blank=False, choices=SETOR_CHOICES)
    dividend_yield_medio_12m = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    vacancia_financeira = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    vacancia_fisica = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    quantidade_ativos = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "FUNDO_IMOBILIARIO"

    def __str__(self):
        return self.codigo_fundo_imobiliario or f"Fundo Imobiliário {self.codigo_fundo_imobiliario}" 
 