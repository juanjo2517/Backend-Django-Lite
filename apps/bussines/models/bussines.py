# Django
from django.db import models

# Utilities
from core.utils.model import LiteModel



class BussinesCompany(LiteModel):
    name_bussines = models.CharField(max_length = 100)
    direction = models.CharField(max_length = 100)
    nit = models.CharField(max_length = 150, unique=True)
    phone = models.CharField(max_length = 150)
    is_active = models.BooleanField(default=True)

    class Meta(LiteModel.Meta):
        db_table = 'bussines_company'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    
