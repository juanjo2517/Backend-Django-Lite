# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilites
from core.utils.model import LiteModel



class User(LiteModel, AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Este Email ya existe'
        }
    )
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Verificacion por correo.'
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

    class Meta(LiteModel.Meta):
        """Meta class."""
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
