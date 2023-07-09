from django.db import models

# Create your models here.


class GaleriaBD(models.Model):

    imagens = models.ImageField(blank=True, upload_to='media')
