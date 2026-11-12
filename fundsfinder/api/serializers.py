# Parte 5 — Criar o Serializer
# importe os recursos necessários do Django REST Framework;
# importe o Model FundoImobiliario;
# crie a classe FundoImobiliarioSerializer utilizando ModelSerializer;
# configure a classe interna Meta;
# associe o Serializer ao Model FundoImobiliario;
# defina os campos que deverão ser representados pelo Serializer;
# observe como os atributos do Model são convertidos em uma representação que poderá ser utilizada na comunicação da API.

from rest_framework import serializers
from api.models import FundoImobiliario

class FundoImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliario
        fields = [
            'id_fundo_imobiliario',
            'codigo_fundo_imobiliario',
            'setor',
            'dividend_yield_medio_12m',
            'vacancia_financeira',
            'vacancia_fisica',
            'quantidade_ativos'
        ]