from django.db import models
from django.db.models.fields import *

# Create your models here.


class Words(models.Model):
    descrip=models.CharField(max_length=20)
    created_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descrip

      


