from django.db import models
# from django.db.models.signals import post_delete
# from django.dispatch import receiver

# Create your models here.

class uploads(models.Model):
    object = None

    pic=models.ImageField(upload_to='pics')
