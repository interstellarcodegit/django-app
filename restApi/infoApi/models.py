from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Updates(models.Model):
    title= models.CharField(max_length=50, unique=True);
    description= models.TextField()
    imageLink= models.TextField(blank=True, null=True)
    image= models.ImageField(null=True, blank=True)
    owner = models.ForeignKey(User, related_name='updates', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering= ['date']