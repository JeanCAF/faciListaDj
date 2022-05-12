#
from model_utils.models import TimeStampedModel
#
from django.db import models


#
class User(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """
    full_name = models.CharField('Nombres', max_length=50,)
    username = models.CharField('username', max_length=30,)
    email = models.EmailField(max_length=50)
    password = models.CharField('password', max_length=15,)
    attachment = models.FileField('foto', blank=True)

    def __str__(self):
        return self.full_name
