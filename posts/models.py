from django.contrib.auth.models import User
from django.db import models

from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    photo = models.ImageField(upload_to='posts/photos', verbose_name='Foto')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Perfil')

    def __str__(self):
        return f'{self.title} by @{self.user.username}'
