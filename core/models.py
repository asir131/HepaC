from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.


User=get_user_model()

class Profile(models.Model):
    age = models.IntegerField()
    sex= models.CharField(max_length=10)
    ALB=models.FloatField(default=0.0)
    ALP=models.FloatField(null=True, blank=True, default=0.0)
    ALT=models.FloatField(null=True, blank=True, default=0.0)
    AST=models.FloatField(null=True, blank=True, default=0.0)
    BIL=models.FloatField(null=True, blank=True, default=0.0)
    CHE=models.FloatField(null=True, blank=True, default=0.0)
    CHOL=models.FloatField(null=True, blank=True, default=0.0)
    CREA=models.FloatField(null=True, blank=True, default=0.0)
    GGT=models.FloatField(null=True, blank=True, default=0.0)
    PROT=models.FloatField(null=True, blank=True, default=0.0)
    comment=models.TextField(null=True, default='')
      
    
def __str__(self):
        return self.user.username