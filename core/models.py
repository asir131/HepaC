from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.


User=get_user_model()

class Profile(models.Model):
    age = models.IntegerField()
    sex= models.CharField(max_length=10)
    ALB=models.IntegerField()
    ALP=models.IntegerField()
    ALT=models.IntegerField()
    AST=models.IntegerField()
    BIL=models.IntegerField()
    CHE=models.IntegerField()
    CHOL=models.IntegerField()
    CREA=models.IntegerField()
    GGT=models.IntegerField()
    PROT=models.IntegerField()
    comment=models.TextField()
      
    
def __str__(self):
        return self.user.username