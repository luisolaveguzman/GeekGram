from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """Proxy model that extends the base data with other information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    website = models.URLField(max_length=255, blank=True, null=True, verbose_name='Website')
    biography = models.TextField(blank=True, null=True, verbose_name='Biografía')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    picture = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    modified = models.DateTimeField(auto_now=True, verbose_name='Actualización')

    def __str__(self):
        return f'{self.user}'
