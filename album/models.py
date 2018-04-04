from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Photo(models.Model):
    category = models.ForeignKey('Category',on_delete = models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)
