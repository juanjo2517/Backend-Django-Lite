""" Bussines Serializer """

# Django Rest
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from apps.bussines.models import BussinesCompany

class BussinesCompanySerializer(serializers.ModelSerializer):
    nit = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=BussinesCompany.objects.all(),
            message="Ya existe una empresa con este NIT."
        )],
    )

    phone = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=BussinesCompany.objects.all(),
            message="Ya existe una empresa con este telefono."
        )],
    )
    class Meta:
        model = BussinesCompany
        exclude = ['modified']
