from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.db.models import Model
from datetime import datetime
# Create your models here.


User=get_user_model()

class Profile(models.Model):
    age = models.IntegerField(blank=False, default=0.0)
    sex= models.CharField(max_length=10)
    ALB=models.FloatField(blank=False, default=0.0)
    ALP=models.FloatField(blank=False, default=0.0)
    ALT=models.FloatField(blank=False, default=0.0)
    AST=models.FloatField(blank=False, default=0.0)
    BIL=models.FloatField(blank=False, default=0.0)
    CHE=models.FloatField(blank=False, default=0.0)
    CHOL=models.FloatField(blank=False, default=0.0)
    CREA=models.FloatField(blank=False, default=0.0)
    GGT=models.FloatField(blank=False, default=0.0)
    PROT=models.FloatField(blank=False, default=0.0)
    comment=models.TextField(null=True, default='')
      
    
def __str__(self):
        return self.user.username