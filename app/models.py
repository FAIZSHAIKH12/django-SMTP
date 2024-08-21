from django.db import models
from django.utils import timezone

class Mymodel(models.Model):
    name=models.CharField(max_length=70)
    mobile=models.CharField(max_length=10,null=False,blank=False)
    email=models.EmailField()
    message=models.TextField()
    submitted_at=models.DateTimeField(default=timezone.now)
    
