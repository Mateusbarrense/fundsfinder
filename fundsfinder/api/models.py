from django.conf.locale import de
from django.db import models

# Create your models here.


class FundoImobiliario(models.Model):

    id_fundo_imobiliario = models.AutoField(primary_key=True)
    codigo_fundo_imobiliario = models.IntegerField(null=False, blank=False)
    setor = models.CharField(max_length=100, null=False, blank=False)
    dividend_yield_medio_12m = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    vacancia_financeira = models.BooleanField(null=True, blank=True) 
    vacancia_fisica = models.BooleanField(null=True, blank=True) 
    quantidade_ativos = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "FUNDO_IMOBILIARIO"

    def __str__(self):
        return self.codigo_fundo_imobiliario or f"Fundo Imobiliário {self.codigo_fundo_imobiliario}" 
 