from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="images/")
    video=models.FileField(upload_to="videos/")
    resume=models.FileField(upload_to="resumes/")
    
